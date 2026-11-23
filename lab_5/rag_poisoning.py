"""Recuperação local com verificação de procedência para um acervo fictício."""

import argparse
from dataclasses import dataclass
from hashlib import sha256
import re
import unicodedata


@dataclass(frozen=True)
class Document:
    document_id: str
    content: str


def content_digest(content):
    return sha256(content.encode("utf-8")).hexdigest()


def tokenize(text):
    normalized = unicodedata.normalize("NFD", text.casefold())
    unaccented = "".join(char for char in normalized if not unicodedata.combining(char))
    stop_words = {"a", "as", "da", "das", "de", "do", "dos", "e", "o", "os", "qual"}
    return set(re.findall(r"[a-z0-9]+", unaccented)) - stop_words


# Neste exercício, o acervo oficial está sob controle do mantenedor.
OFFICIAL_DOCUMENTS = (
    Document("oficial-biblioteca", "A biblioteca da Vila Aurora fecha às 18h."),
    Document("oficial-museu", "O museu da Vila Aurora abre às 10h."),
)
APPROVED_DIGESTS = {
    document.document_id: content_digest(document.content)
    for document in OFFICIAL_DOCUMENTS
}

# Os candidatos representam a saída de uma busca em um índice misto.
CANDIDATES = (
    Document("rascunho-biblioteca", "A biblioteca da Vila Aurora fecha às 23h."),
    *OFFICIAL_DOCUMENTS,
)


def retrieve(question, candidates, approved_digests):
    question_tokens = tokenize(question)
    matches = {}
    for document in candidates:
        approved_digest = approved_digests.get(document.document_id)
        if approved_digest != content_digest(document.content):
            continue
        if question_tokens & tokenize(document.content):
            matches[document.document_id] = document
    return tuple(matches.values())


def answer(question, candidates=CANDIDATES):
    documents = retrieve(question, candidates, APPROVED_DIGESTS)
    if not documents:
        return "Nenhuma fonte aprovada corresponde à pergunta."
    return "\n".join(f"[{doc.document_id}] {doc.content}" for doc in documents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pergunta", required=True, help="Consulta ao acervo fictício")
    args = parser.parse_args()
    print(answer(args.pergunta))


if __name__ == "__main__":
    main()
