# Lab 4 · Confused Deputy

**Português (Brasil)** · [English](README.en.md) · [Catálogo](../README.md)

O modelo devolve texto e o orquestrador usa verificações textuais para decidir se simula uma ação. Observe a fronteira entre a saída do modelo e a autorização da aplicação. A ação é registrada no console.

## Execute no PowerShell

A partir da raiz, use o ambiente preparado na seção [Labs 1 a 4 com provedor](../README.md#labs-1-a-4-com-provedor). O resultado depende do provedor configurado. Use dados fictícios e escopo autorizado.

```powershell
& $labPython -I -B -X utf8 .\lab_4\teste_confused_deputy.py
```
