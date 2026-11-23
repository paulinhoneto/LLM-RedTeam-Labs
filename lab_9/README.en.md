# Lab 9 · Guardrails and evaluation

[Português (Brasil)](README.md) · **English** · [Catalog](../README.en.md)

The two filters process the same six labeled responses. The keyword filter misses 2 of 3 prohibited responses and blocks 1 of 3 legitimate ones. The marker filter misses 1 of 3 and blocks none of the legitimate responses. `VP`, `FN`, `FP`, and `VN` mean true positive, false negative, false positive, and true negative.

## Run in PowerShell

From the repository root, use the offline virtual environment from the [English quick start](../README.en.md#quick-start-on-windows). The command flags and console output use Portuguese.

```powershell
& $labPython -I -B -X utf8 .\lab_9\guardrail_evaluation.py --filtro comparar
```
