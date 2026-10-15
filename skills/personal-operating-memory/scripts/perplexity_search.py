#!/usr/bin/env python3
"""Small Perplexity Search/Sonar helper for Personal Operating Memory."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


API_BASE = "https://api.perplexity.ai"


def post_json(path: str, payload: dict) -> dict:
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        raise SystemExit(
            "PERPLEXITY_API_KEY is not set. Set it in your local shell or secret manager; do not write it into the vault."
        )

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Perplexity API error {error.code}: {body}") from error


def add_common_filters(payload: dict, args: argparse.Namespace) -> None:
    if args.domain:
        payload["search_domain_filter"] = args.domain
    if args.language:
        payload["search_language_filter"] = args.language
    if args.recency:
        payload["search_recency_filter"] = args.recency
    if args.country:
        payload["country"] = args.country


def run_search(args: argparse.Namespace) -> dict:
    payload: dict = {
        "query": args.query,
        "max_results": args.max_results,
    }
    add_common_filters(payload, args)
    if args.context:
        payload["search_context_size"] = args.context
    return post_json("/search", payload)


def run_sonar(args: argparse.Namespace) -> dict:
    payload: dict = {
        "model": args.model,
        "messages": [{"role": "user", "content": args.query}],
    }
    if args.max_tokens:
        payload["max_tokens"] = args.max_tokens
    if args.temperature is not None:
        payload["temperature"] = args.temperature
    if args.context:
        payload["web_search_options"] = {"search_context_size": args.context}
    if args.recency:
        payload["search_recency_filter"] = args.recency
    if args.domain:
        payload["search_domain_filter"] = args.domain
    if args.language:
        payload["search_language_filter"] = args.language
    return post_json("/v1/sonar", payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Call Perplexity Search API or Sonar API without storing secrets."
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    search = subparsers.add_parser("search", help="Return ranked raw web results.")
    search.add_argument("query")
    search.add_argument("--max-results", type=int, default=10)
    search.add_argument("--context", choices=["low", "medium", "high"])
    add_filter_args(search)

    sonar = subparsers.add_parser("sonar", help="Return a cited web-grounded answer.")
    sonar.add_argument("query")
    sonar.add_argument(
        "--model",
        default="sonar-pro",
        choices=["sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning-pro"],
    )
    sonar.add_argument("--max-tokens", type=int)
    sonar.add_argument("--temperature", type=float)
    sonar.add_argument("--context", choices=["low", "medium", "high"], default="low")
    add_filter_args(sonar)

    return parser


def add_filter_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--domain",
        action="append",
        help="Restrict results to a domain. Repeat for multiple domains.",
    )
    parser.add_argument(
        "--language",
        action="append",
        help="Restrict results by ISO 639-1 language code. Repeat for multiple languages.",
    )
    parser.add_argument("--country", help="ISO 3166-1 alpha-2 country code.")
    parser.add_argument("--recency", choices=["hour", "day", "week", "month", "year"])


def main() -> int:
    args = build_parser().parse_args()
    result = run_search(args) if args.mode == "search" else run_sonar(args)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
