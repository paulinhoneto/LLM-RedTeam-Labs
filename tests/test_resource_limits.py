from pathlib import Path
import sys
import unittest
from unittest.mock import Mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_10.resource_limits import InferenceGateway, MAX_CALLS_PER_ACCOUNT, MAX_PROMPT_CHARS


class ResourceLimitsTests(unittest.TestCase):
    def setUp(self):
        self.model = Mock(return_value="Resposta simulada.")
        self.gateway = InferenceGateway(self.model)

    def test_prompt_at_length_limit_reaches_model(self):
        prompt = "x" * MAX_PROMPT_CHARS
        self.assertEqual(self.gateway.submit("ana", prompt), "Resposta simulada.")
        self.model.assert_called_once_with(prompt)

    def test_invalid_input_neither_calls_model_nor_spends_quota(self):
        for prompt in (None, " ", "x" * (MAX_PROMPT_CHARS + 1)):
            with self.subTest(prompt=prompt):
                self.gateway.submit("ana", prompt)
        self.model.assert_not_called()
        self.assertEqual(self.gateway.calls_by_account["ana"], 0)

    def test_exhausted_account_cannot_call_model_again(self):
        for _ in range(MAX_CALLS_PER_ACCOUNT):
            self.gateway.submit("ana", "Resuma a nota.")
        self.assertEqual(self.gateway.submit("ana", "Liste os horários."), "Cota da conta esgotada.")
        self.assertEqual(self.model.call_count, MAX_CALLS_PER_ACCOUNT)

    def test_another_account_has_its_own_quota(self):
        for _ in range(MAX_CALLS_PER_ACCOUNT):
            self.gateway.submit("ana", "Resuma a nota.")
        self.assertEqual(self.gateway.submit("bruno", "Liste os horários."), "Resposta simulada.")
        self.assertEqual(self.model.call_count, MAX_CALLS_PER_ACCOUNT + 1)
