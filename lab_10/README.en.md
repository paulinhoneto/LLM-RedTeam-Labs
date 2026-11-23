# Lab 10 · Unbounded consumption

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The gateway allows two calls per account and limits input length. The demo submits five requests. Three reach the simulated model. The oversized input and the request from an account out of quota are rejected before inference.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_10\resource_limits.py
```
