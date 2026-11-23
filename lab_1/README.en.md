# Lab 1 · Direct prompt injection

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The script sends a fixed text transformation request as the user message. It prints the provider response. A response that performs the transformation shows task compliance. Assessing a guardrail requires a separately defined policy and expected outcome.

## Run in PowerShell

From the repository root, use the provider environment from [Running Labs 1–4 with a provider](../README.en.md#running-labs-14-with-a-provider). Responses depend on the configured provider. Use fictional data in an authorized setting. The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_1\teste_sms.py
```
