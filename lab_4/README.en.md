# Lab 4 · Confused deputy

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The model returns text and the orchestrator uses text checks to decide whether to simulate an action. Observe the boundary between model output and application authorization. The action is printed to the console.

## Run in PowerShell

From the repository root, use the provider environment from [Running Labs 1–4 with a provider](../README.en.md#running-labs-14-with-a-provider). Responses depend on the configured provider. Use fictional data in an authorized setting. The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_4\teste_confused_deputy.py
```
