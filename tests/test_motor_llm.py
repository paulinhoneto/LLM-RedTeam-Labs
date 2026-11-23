import importlib.util
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch


class MotorTests(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.client.chat.return_value = SimpleNamespace(text="Resumo local")
        fake_dotenv = SimpleNamespace(load_dotenv=Mock())
        fake_freelm = SimpleNamespace(
            FreeLLM=SimpleNamespace(from_env=Mock(return_value=self.client))
        )
        source = Path(__file__).resolve().parents[1] / "motor_llm.py"
        spec = importlib.util.spec_from_file_location("test_motor_instance", source)
        self.motor = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"dotenv": fake_dotenv, "freelm": fake_freelm}):
            spec.loader.exec_module(self.motor)

    def test_default_route_preserves_language_instruction(self):
        self.assertEqual(self.motor.perguntar_ia("Resuma."), "Resumo local")
        messages = self.client.chat.call_args.args[0]
        self.assertEqual([message["role"] for message in messages], ["system", "user"])
        self.assertEqual(messages[-1]["content"], "Resuma.")
        self.assertEqual(self.client.chat.call_args.kwargs, {"model": "auto"})

    def test_tools_route_preserves_context_and_task(self):
        self.motor.perguntar_ia("Resuma.", "Documento fictício.", True)
        self.client.chat.assert_called_once_with(
            [
                {"role": "user", "content": "Contexto para análise:\nDocumento fictício."},
                {"role": "user", "content": "Resuma."},
            ],
            model="chat:tools",
        )

    def test_chat_error_is_reported_as_text(self):
        self.client.chat.side_effect = RuntimeError("falha simulada")
        result = self.motor.perguntar_ia("Resuma.")
        self.assertTrue(result.startswith("Erro na IA:"))


if __name__ == "__main__":
    unittest.main()
