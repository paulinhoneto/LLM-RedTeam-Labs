# Lab 8 · User data isolation

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

Run the command again with `--sessao bruno` to see the same note ID resolve to a different account's note. Only Bruno can read `NOTA-02`. Ana receives the same unavailable message for that note and for a nonexistent note.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao ana --nota NOTA-01
```
