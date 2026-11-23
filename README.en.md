# LLM-RedTeam-Labs

[Português (Brasil)](README.md) · **English**

Python labs for learning how to secure applications that use large language models (LLMs). The exercises use fictional data to explore controls such as document provenance, tool authorization, data isolation, output filtering, and resource limits.

## Quick start on Windows

Run these PowerShell commands from the repository root. If you already have a working `env` virtual environment, skip the first command.

```powershell
python -m venv --without-pip .\env
$labPython = '.\env\Scripts\python.exe'
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario outro-titular
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

Labs 5–10 and the test suite run offline using only the Python standard library. In the Lab 6 example, `outro-titular` selects a session that requests access to a ticket owned by someone else. Expect `Negado` (denied) and `Depois: aberto` (after: open). Scripts and their output use Portuguese CLI labels.

## Lab catalog

| Lab | Topic | What to look for |
| --- | --- | --- |
| [1](lab_1/README.en.md) | Direct prompt injection | The script sends a text transformation request as a user message. |
| [2](lab_2/README.en.md) | Indirect prompt injection | The model receives a fictional log as context. |
| [3](lab_3/README.en.md) | Chained injection and Markdown | The orchestrator examines model output and simulates an action in the console. |
| [4](lab_4/README.en.md) | Confused deputy | The simulated orchestrator illustrates the risk of treating model text as an action decision. |
| [5](lab_5/README.en.md) | RAG poisoning | Only candidates matching the approved document catalog reach retrieval results. |
| [6](lab_6/README.en.md) | Tool calling | Permission and ownership determine whether a simulated ticket closes. |
| [7](lab_7/README.en.md) | MCP security | A simulated tool call must satisfy both input validation and session scope. |
| [8](lab_8/README.en.md) | User data isolation | Two accounts can use the same note ID without sharing data. |
| [9](lab_9/README.en.md) | Guardrails and evaluation | Two output filters are compared using false negatives and false positives. |
| [10](lab_10/README.en.md) | Unbounded consumption | Input size and per-account quotas are checked before simulated inference. |

## Running Labs 1–4 with a provider

These labs use [`motor_llm.py`](motor_llm.py) and FreeLLM to call a model provider. If you have authorization to use a provider, create a separate virtual environment with pip and install the dependencies.

```powershell
python -m venv .\venv
$labPython = '.\venv\Scripts\python.exe'
& $labPython -m pip install -r .\requirements.txt
```

Set your provider's environment variable locally in the repository-root `.env` file, for example `GROQ_API_KEY` for Groq. Git ignores that file. From the repository root, run the selected script with the same Python executable.

```powershell
& $labPython -I -B -X utf8 .\lab_1\teste_sms.py
```

## Further reading

The [project guide](docs/PROJECT-GUIDE.md), [historical reports](docs/), [roadmap](docs/ROADMAP.md), and detailed lab guides are in Brazilian Portuguese.

Use fictional data and keep exercises within local, owned, or explicitly authorized environments. When reporting results, distinguish local simulations from observations made through a real provider.
