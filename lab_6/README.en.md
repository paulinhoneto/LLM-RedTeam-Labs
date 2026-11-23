# Lab 6 · Tool calling and authorization

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The same simulated call proposes closing ticket `CH-01`. With `outro-titular` (another owner), the result is denied and the ticket remains open. Try `autorizado` to see it close and `sem-permissao` to see an owner without permission denied.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario outro-titular
```
