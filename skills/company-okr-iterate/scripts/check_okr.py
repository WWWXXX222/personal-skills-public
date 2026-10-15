#!/usr/bin/env python3
"""Check an OKR draft's structure; never infer approval or business validity."""
import argparse
import json
import math
import re
from datetime import date
from pathlib import Path


class Check:
    def __init__(self):
        self.findings = []
        self.source_ids = set()
        self.kr_ids = set()
        self.ids = set()
        self.graph = {}

    def add(self, severity, code, path, message):
        self.findings.append(dict(severity=severity, code=code, path=path, message=message))

    def error(self, path, message):
        self.add("error", "INVALID_STRUCTURE", path, message)

    def text(self, value, path, nullable=False):
        if value is None and nullable:
            self.add("open", "UNKNOWN_FIELD", path, "Unknown; requires evidence or a decision.")
        elif not isinstance(value, str) or not value.strip():
            self.error(path, "Expected nonempty text.")

    def array(self, value, path, nonempty=False):
        if not isinstance(value, list):
            self.error(path, "Expected an array.")
            return []
        if nonempty and not value:
            self.error(path, "Array must not be empty.")
        return value

    def obj(self, value, path):
        if not isinstance(value, dict):
            self.error(path, "Expected an object.")
            return {}
        return value

    def iso_date(self, value, path, nullable=False):
        if value is None and nullable:
            self.add("open", "UNKNOWN_FIELD", path, "Deadline is unknown.")
            return None
        if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            try:
                return date.fromisoformat(value)
            except ValueError:
                pass
        self.error(path, "Expected a valid YYYY-MM-DD date.")
        return None

    def identifier(self, value, path, known):
        if not isinstance(value, str) or not value.strip():
            self.error(path, "Expected a nonempty ID.")
        elif value in known:
            self.add("error", "DUPLICATE_ID", path, f"Duplicate ID: {value}")
        else:
            known.add(value)

    def links(self, value, path, known, self_id=None):
        links = self.array(value, path)
        valid = []
        for i, ref in enumerate(links):
            where = f"{path}[{i}]"
            if not isinstance(ref, str) or ref not in known:
                self.add("error", "BROKEN_REFERENCE", where, "Reference does not identify a declared record.")
            elif self_id is not None and ref == self_id:
                self.add("error", "SELF_REFERENCE", where, "A KR cannot reference itself.")
            elif ref in valid:
                self.error(where, "Duplicate reference.")
            else:
                valid.append(ref)
        return valid

    def fact(self, value, path, owner=False):
        fact = self.obj(value, path)
        if "value" not in fact:
            self.error(path + ".value", "Missing value; use null for unknown.")
        status = fact.get("status")
        val = fact.get("value")
        refs = self.links(fact.get("source_ids"), path + ".source_ids", self.source_ids)
        if not isinstance(status, str) or status not in {"confirmed", "proposed", "unknown"}:
            self.error(path + ".status", "Expected confirmed, proposed, or unknown.")
            return
        if status == "unknown":
            if val is not None:
                self.error(path + ".value", "Unknown facts must use null, not a guessed value.")
        else:
            valid = isinstance(val, str) and bool(val.strip())
            if not owner:
                valid = valid or (type(val) is int or (type(val) is float and math.isfinite(val)))
            if not valid:
                self.error(path + ".value", "Expected a nonempty name." if owner else "Expected nonempty text or a finite number.")
        if status == "confirmed" and not refs:
            self.add("error", "UNSOURCED_CONFIRMED", path, "A confirmed field needs at least one declared source.")
        if status != "confirmed":
            self.add("open", "UNCONFIRMED_FIELD", path, f"Field remains {status}; do not present it as approved or observed.")

    def run(self, data):
        data = self.obj(data, "$")
        if type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
            self.error("schema_version", "Expected integer 1.")
        self.text(data.get("company"), "company")
        period = self.obj(data.get("period"), "period")
        start = self.iso_date(period.get("start"), "period.start")
        end = self.iso_date(period.get("end"), "period.end")
        if start and end and start > end:
            self.error("period", "Start must not be after end.")
        for i, source in enumerate(self.array(data.get("sources"), "sources")):
            path = f"sources[{i}]"
            source = self.obj(source, path)
            self.identifier(source.get("id"), path + ".id", self.source_ids)
            self.text(source.get("locator"), path + ".locator")
        krs = []
        for i, objective in enumerate(self.array(data.get("objectives"), "objectives", True)):
            path = f"objectives[{i}]"
            objective = self.obj(objective, path)
            self.identifier(objective.get("id"), path + ".id", self.ids)
            self.text(objective.get("title"), path + ".title")
            for j, kr in enumerate(self.array(objective.get("krs"), path + ".krs", True)):
                where = f"{path}.krs[{j}]"
                kr = self.obj(kr, where)
                self.identifier(kr.get("id"), where + ".id", self.ids)
                if isinstance(kr.get("id"), str) and kr["id"].strip():
                    self.kr_ids.add(kr["id"])
                krs.append((where, kr))
        for path, kr in krs:
            self.text(kr.get("title"), path + ".title")
            kind = kr.get("kind")
            if not isinstance(kind, str) or kind not in {"outcome", "enabler", "experiment"}:
                self.error(path + ".kind", "Expected outcome, enabler, or experiment.")
            metric = self.obj(kr.get("metric"), path + ".metric")
            for field in ("definition", "unit", "population", "window"):
                if field not in metric:
                    self.error(path + ".metric." + field, "Missing field; use null for unknown.")
                else:
                    self.text(metric[field], path + ".metric." + field, True)
            for field in ("owner", "baseline", "target"):
                self.fact(kr.get(field), path + "." + field, owner=field == "owner")
            for field in ("deadline", "verification"):
                if field not in kr:
                    self.error(path + "." + field, "Missing field; use null for unknown.")
            due = self.iso_date(kr.get("deadline"), path + ".deadline", True)
            if due and start and end and not start <= due <= end:
                self.add("error", "OUTSIDE_PERIOD", path + ".deadline", "KR deadline is outside the planning period.")
            self.text(kr.get("verification"), path + ".verification", True)
            deps = self.links(kr.get("dependencies"), path + ".dependencies", self.kr_ids, kr.get("id"))
            supports = self.links(kr.get("supports"), path + ".supports", self.kr_ids, kr.get("id"))
            if kind == "enabler" and not supports:
                self.add("error", "UNLINKED_ENABLER", path + ".supports", "An enabler needs a supported KR.")
            if isinstance(kr.get("id"), str):
                self.graph[kr["id"]] = deps
            questions = self.array(kr.get("open_questions"), path + ".open_questions")
            for i, question in enumerate(questions):
                self.text(question, f"{path}.open_questions[{i}]")
            if questions:
                self.add("open", "OPEN_QUESTIONS", path + ".open_questions", "Carry these questions into the handoff.")
        remaining = {key: set(value) for key, value in self.graph.items()}
        while remaining:
            ready = {key for key, value in remaining.items() if not value.intersection(remaining)}
            if not ready:
                self.add("error", "DEPENDENCY_CYCLE", "dependencies", "Cycle detected; review these KRs and their dependencies: " + ", ".join(sorted(remaining)))
                break
            remaining = {key: value for key, value in remaining.items() if key not in ready}
        failed = any(x["severity"] == "error" for x in self.findings)
        gaps = any(x["severity"] == "open" for x in self.findings)
        return {
            "structure": "FAIL" if failed else "PASS",
            "readiness": "NOT_CHECKED" if failed else "DATA_GAPS" if gaps else "REVIEW_REQUIRED",
            "scope": "Structural checks only; sources, strategy, capacity, approval, and Markdown parity require independent review.",
            "findings": self.findings,
        }


def validate(data):
    return Check().run(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"structure": "FAIL", "readiness": "NOT_CHECKED", "input_error": str(exc)}, ensure_ascii=False))
        return 2
    report = validate(data)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(report["structure"] == "FAIL")


if __name__ == "__main__":
    raise SystemExit(main())
