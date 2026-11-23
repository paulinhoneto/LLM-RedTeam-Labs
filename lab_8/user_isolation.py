"""Demonstração offline de isolamento de notas entre contas fictícias."""

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    account_id: str


SESSIONS = {"ana": Session("conta-ana"), "bruno": Session("conta-bruno")}
NOTES_BY_ACCOUNT = {
    "conta-ana": {"NOTA-01": "Ana: revisar o catálogo."},
    "conta-bruno": {
        "NOTA-01": "Bruno: organizar a agenda.",
        "NOTA-02": "Bruno: preparar o relatório.",
    },
}


def read_note(session, note_id):
    account_notes = NOTES_BY_ACCOUNT.get(session.account_id, {})
    return account_notes.get(note_id)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sessao", choices=SESSIONS, required=True)
    parser.add_argument("--nota", required=True)
    args = parser.parse_args()

    content = read_note(SESSIONS[args.sessao], args.nota)
    if content is None:
        print("Nota indisponível nesta sessão.")
    else:
        print(content)


if __name__ == "__main__":
    main()
