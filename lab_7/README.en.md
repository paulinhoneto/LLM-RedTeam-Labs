# Lab 7 · MCP security

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

An in-memory handler checks a simulated MCP `tools/call` message and the session scope. Expect `isError: true` and an access-denied message. Try `autorizado` for a successful read or `entrada-invalida` for input validation. The exercise uses no running MCP server.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_7\mcp_security.py --cenario sem-permissao
```
