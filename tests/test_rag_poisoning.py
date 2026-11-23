from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lab_5.rag_poisoning import Document, OFFICIAL_DOCUMENTS, answer


class RagPoisoningTests(unittest.TestCase):
    def test_uses_only_approved_sources(self):
        self.assertEqual(
            answer("Qual é o horário da biblioteca?"),
            "[oficial-biblioteca] A biblioteca da Vila Aurora fecha às 18h.",
        )

    def test_preserves_valid_version_when_candidate_content_changes(self):
        official = OFFICIAL_DOCUMENTS[0]
        changed = Document(official.document_id, "A biblioteca está fechada.")
        self.assertEqual(
            answer("biblioteca", (changed,)),
            "Nenhuma fonte aprovada corresponde à pergunta.",
        )
        self.assertEqual(
            answer("biblioteca", (changed, official)),
            f"[{official.document_id}] {official.content}",
        )

    def test_unknown_topic_has_no_approved_source(self):
        self.assertEqual(
            answer("Onde fica a farmácia?"), "Nenhuma fonte aprovada corresponde à pergunta."
        )

    def test_cli_accepts_question_and_prints_source(self):
        result = subprocess.run(
            [
                sys.executable, "-I", "-B", "-X", "utf8",
                str(ROOT / "lab_5" / "rag_poisoning.py"),
                "--pergunta", "Horário do museu?",
            ],
            check=True,
            capture_output=True,
            encoding="utf-8",
        )
        self.assertEqual(
            result.stdout.strip(), "[oficial-museu] O museu da Vila Aurora abre às 10h."
        )
