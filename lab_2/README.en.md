# Lab 2 · Indirect prompt injection

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The script submits a task and a separate fictional log to the model. The console shows the model's text. The script selects a tool-capable route, with no registered tool execution.

## Run in PowerShell

From the repository root, use the provider environment from [Running Labs 1–4 with a provider](../README.en.md#running-labs-14-with-a-provider). Responses depend on the configured provider. Use fictional data in an authorized setting. The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_2\teste_injecao_indireta.py
```
