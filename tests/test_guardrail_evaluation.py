from collections import Counter
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_9.guardrail_evaluation import (
    CASES,
    evaluate,
    format_rate,
    keyword_guardrail,
    marker_guardrail,
)


class GuardrailEvaluationTests(unittest.TestCase):
    def test_keyword_baseline_measures_all_four_outcomes(self):
        counts = Counter(outcome for _, outcome in evaluate(CASES, keyword_guardrail))
        self.assertEqual(counts, {"VP": 1, "FN": 2, "FP": 1, "VN": 2})

    def test_marker_reduces_missed_cases_and_false_positives(self):
        counts = Counter(outcome for _, outcome in evaluate(CASES, marker_guardrail))
        self.assertEqual(counts, {"VP": 2, "FN": 1, "VN": 3})

    def test_marker_report_exposes_remaining_gap(self):
        results = dict(evaluate(CASES, marker_guardrail))
        self.assertEqual(results["agenda-privada"], "FN")
        self.assertEqual(results["manual-publico"], "VN")

    def test_rate_preserves_denominator_and_handles_empty_group(self):
        self.assertEqual(format_rate(1, 3), "1/3 (33.3%)")
        self.assertEqual(format_rate(0, 0), "n/a")
