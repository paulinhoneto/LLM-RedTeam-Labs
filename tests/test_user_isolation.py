from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_8.user_isolation import SESSIONS, Session, read_note


class UserIsolationTests(unittest.TestCase):
    def test_same_note_id_resolves_in_each_accounts_scope(self):
        self.assertEqual(read_note(SESSIONS["ana"], "NOTA-01"), "Ana: revisar o catálogo.")
        self.assertEqual(read_note(SESSIONS["bruno"], "NOTA-01"), "Bruno: organizar a agenda.")

    def test_note_available_to_owner_is_unavailable_to_other_account(self):
        self.assertEqual(
            read_note(SESSIONS["bruno"], "NOTA-02"), "Bruno: preparar o relatório."
        )
        self.assertIsNone(read_note(SESSIONS["ana"], "NOTA-02"))

    def test_unknown_account_has_no_access(self):
        self.assertIsNone(read_note(Session("conta-inexistente"), "NOTA-01"))

    def test_cli_reports_foreign_and_missing_notes_the_same_way(self):
        for note_id in ("NOTA-02", "NOTA-99"):
            with self.subTest(note_id=note_id):
                result = subprocess.run(
                    [
                        sys.executable, "-I", "-B", "-X", "utf8",
                        str(ROOT / "lab_8" / "user_isolation.py"),
                        "--sessao", "ana", "--nota", note_id,
                    ],
                    check=True,
                    capture_output=True,
                    encoding="utf-8",
                )
                self.assertEqual(result.stdout.strip(), "Nota indisponível nesta sessão.")
