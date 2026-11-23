# Lab 5 · RAG poisoning and provenance

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The query means “What are the library hours?” The approved source reports a closing time of **18:00**, while the unapproved draft is excluded. The retriever checks the document ID and the SHA-256 hash against a trusted catalog. The output is the selected source text.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_5\rag_poisoning.py --pergunta "Qual é o horário da biblioteca?"
```
