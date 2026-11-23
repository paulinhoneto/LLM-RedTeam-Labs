from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_7.mcp_security import build_call, handle_request


class McpSecurityTests(unittest.TestCase):
    def setUp(self):
        self.request = build_call("CARD-001")
        self.allowed = frozenset({"CARD-001"})

    def test_authorized_read_returns_card_and_request_id(self):
        response = handle_request(self.request, self.allowed)
        self.assertEqual(response["id"], self.request["id"])
        self.assertFalse(response["result"]["isError"])
        self.assertEqual(
            response["result"]["content"][0]["text"],
            "Vila Aurora: reunião fictícia às 14h.",
        )

    def test_valid_request_outside_scope_discloses_no_content(self):
        response = handle_request(self.request, frozenset())
        self.assertTrue(response["result"]["isError"])
        self.assertEqual(
            response["result"]["content"], [{"type": "text", "text": "Acesso negado ao cartão."}]
        )

    def test_invalid_arguments_return_tool_errors(self):
        for arguments in ({}, {"card_id": 1}, {"card_id": ""}, {"card_id": "CARD-001", "extra": True}):
            with self.subTest(arguments=arguments):
                self.request["params"]["arguments"] = arguments
                result = handle_request(self.request, self.allowed)["result"]
                self.assertTrue(result["isError"])
                self.assertTrue(result["content"][0]["text"].startswith("Entrada inválida"))

    def test_unknown_tool_returns_protocol_error(self):
        self.request["params"]["name"] = "unknown"
        self.assertEqual(handle_request(self.request, self.allowed)["error"]["code"], -32602)

    def test_unknown_method_returns_protocol_error(self):
        self.request["method"] = "unknown"
        self.assertEqual(handle_request(self.request, self.allowed)["error"]["code"], -32601)

    def test_invalid_request_returns_protocol_error(self):
        self.assertEqual(handle_request([], self.allowed)["error"]["code"], -32600)
