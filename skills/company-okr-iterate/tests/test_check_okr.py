import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('check_okr', ROOT / 'scripts/check_okr.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class OkrCheckTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'assets/okr.example.json').read_text())
        self.kr = self.data['objectives'][0]['krs'][0]

    def check_codes(self, *codes):
        result = CHECK.validate(self.data)
        observed = {f['code'] for f in result['findings']}
        self.assertTrue(set(codes) <= observed, result)
        return result

    def test_complete_draft_still_needs_independent_review(self):
        report = CHECK.validate(self.data)
        self.assertEqual(report['structure'], 'PASS')
        self.assertEqual(report['readiness'], 'REVIEW_REQUIRED')

    def test_unknown_baseline_remains_gap_without_fabrication(self):
        self.kr['baseline'] = dict(value=None, status='unknown', source_ids=[])
        report = self.check_codes('UNCONFIRMED_FIELD')
        self.assertEqual(report['structure'], 'PASS')
        self.assertEqual(report['readiness'], 'DATA_GAPS')

    def test_unknown_does_not_hide_a_guessed_value(self):
        self.kr['baseline']['status'] = 'unknown'
        self.assertEqual(self.check_codes('INVALID_STRUCTURE')['structure'], 'FAIL')

    def test_proposed_target_never_reads_as_confirmed(self):
        self.kr['target']['status'] = 'proposed'
        self.kr['target']['source_ids'] = []
        self.assertEqual(CHECK.validate(self.data)['readiness'], 'DATA_GAPS')

    def test_confirmed_value_requires_declared_evidence(self):
        self.kr['target']['source_ids'] = []
        self.check_codes('UNSOURCED_CONFIRMED')

    def test_broken_source_reference_is_not_evidence(self):
        self.kr['target']['source_ids'] = ['missing']
        self.check_codes('BROKEN_REFERENCE', 'UNSOURCED_CONFIRMED')

    def test_zero_baseline_is_not_missing(self):
        self.kr['baseline']['value'] = 0
        self.assertEqual(CHECK.validate(self.data)['structure'], 'PASS')

    def test_malformed_fact_types_do_not_crash(self):
        for value in (True, float('inf'), {}, [], ''):
            with self.subTest(value=value):
                self.kr['target']['value'] = value
                self.assertEqual(CHECK.validate(self.data)['structure'], 'FAIL')
        self.kr['target']['status'] = []
        self.assertEqual(CHECK.validate(self.data)['structure'], 'FAIL')

    def test_duplicate_kr_ids_are_rejected(self):
        self.data['objectives'][0]['krs'].append(copy.deepcopy(self.kr))
        self.check_codes('DUPLICATE_ID')

    def test_unavailable_metric_is_a_gap_not_a_complete_definition(self):
        self.kr['metric']['population'] = None
        self.assertEqual(CHECK.validate(self.data)['readiness'], 'DATA_GAPS')
        del self.kr['metric']['population']
        self.assertEqual(CHECK.validate(self.data)['structure'], 'FAIL')

    def test_deadline_cannot_silently_move_to_next_quarter(self):
        self.kr['deadline'] = '2031-01-01'
        self.check_codes('OUTSIDE_PERIOD')

    def test_bad_dates_are_rejected(self):
        self.kr['deadline'] = '2030-11-31'
        self.check_codes('INVALID_STRUCTURE')

    def test_forward_reference_and_enabler_are_supported(self):
        other = copy.deepcopy(self.kr)
        other.update(id='O1.KR2', kind='enabler', supports=['O1.KR1'])
        self.kr['dependencies'] = ['O1.KR2']
        self.data['objectives'][0]['krs'].append(other)
        self.assertEqual(CHECK.validate(self.data)['structure'], 'PASS')

    def test_circular_delivery_dependencies_are_rejected(self):
        other = copy.deepcopy(self.kr)
        other.update(id='O1.KR2', dependencies=['O1.KR1'])
        self.kr['dependencies'] = ['O1.KR2']
        self.data['objectives'][0]['krs'].append(other)
        self.check_codes('DEPENDENCY_CYCLE')

    def test_missing_self_reference_and_unlinked_enabler(self):
        self.kr.update(kind='enabler', dependencies=['absent'], supports=['O1.KR1'])
        self.check_codes('BROKEN_REFERENCE', 'SELF_REFERENCE', 'UNLINKED_ENABLER')

    def test_open_business_questions_do_not_disappear(self):
        self.kr['open_questions'] = ['Which approved capacity supports this target?']
        self.assertEqual(self.check_codes('OPEN_QUESTIONS')['readiness'], 'DATA_GAPS')

    def test_wrong_document_shapes_return_findings(self):
        for value in (None, [], 'text', {'objectives': [None]}):
            with self.subTest(value=value):
                self.assertEqual(CHECK.validate(value)['structure'], 'FAIL')

    def test_cli_reports_failures_and_never_changes_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'draft.json'
            for content, expected_code in (('{', 2), (json.dumps(self.data), 0), ('{}', 1)):
                path.write_text(content)
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_okr.py'), str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected_code, result.stderr)
                self.assertIn('structure', json.loads(result.stdout))
                self.assertEqual(path.read_text(), content)


if __name__ == '__main__':
    unittest.main()
