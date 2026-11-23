from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_6.tool_calling import Principal, Ticket, dispatch


class ToolCallingTests(unittest.TestCase):
    def setUp(self):
        self.tickets = {"CH-01": Ticket(owner_id="ana")}
        self.owner = Principal("ana", True)
        self.arguments = {"ticket_id": "CH-01"}

    def test_owner_with_permission_can_close_ticket(self):
        result = dispatch(self.owner, "close_ticket", self.arguments, self.tickets)
        self.assertEqual(result, "Permitido: chamado fechado.")
        self.assertEqual(self.tickets["CH-01"].status, "fechado")

    def test_other_owner_cannot_close_ticket(self):
        result = dispatch(Principal("bruno", True), "close_ticket", self.arguments, self.tickets)
        self.assertTrue(result.startswith("Negado:"))
        self.assertEqual(self.tickets["CH-01"].status, "aberto")

    def test_owner_without_permission_cannot_close_ticket(self):
        result = dispatch(Principal("ana", False), "close_ticket", self.arguments, self.tickets)
        self.assertTrue(result.startswith("Negado:"))
        self.assertEqual(self.tickets["CH-01"].status, "aberto")

    def test_unknown_tool_is_denied(self):
        result = dispatch(self.owner, "unknown", self.arguments, self.tickets)
        self.assertEqual(result, "Negado: ferramenta desconhecida.")
        self.assertEqual(self.tickets["CH-01"].status, "aberto")

    def test_invalid_arguments_are_denied(self):
        for arguments in (None, {}, {"ticket_id": []}, {"ticket_id": "CH-01", "extra": True}):
            with self.subTest(arguments=arguments):
                result = dispatch(self.owner, "close_ticket", arguments, self.tickets)
                self.assertEqual(result, "Negado: argumentos inválidos.")
                self.assertEqual(self.tickets["CH-01"].status, "aberto")

    def test_missing_ticket_is_denied(self):
        result = dispatch(self.owner, "close_ticket", {"ticket_id": "CH-02"}, self.tickets)
        self.assertTrue(result.startswith("Negado:"))
        self.assertEqual(self.tickets["CH-01"].status, "aberto")
