# Lab 1 · Injeção direta

**Português (Brasil)** · [English](README.en.md) · [Catálogo](../README.md)

O script envia um pedido fixo de transformação de texto como mensagem do usuário e exibe a resposta do provedor. Cumprir o pedido demonstra a transformação. Para avaliar um guardrail, defina antes a política e o resultado esperado.

## Execute no PowerShell

A partir da raiz, use o ambiente preparado na seção [Labs 1 a 4 com provedor](../README.md#labs-1-a-4-com-provedor). O resultado depende do provedor configurado. Use dados fictícios e escopo autorizado.

```powershell
& $labPython -I -B -X utf8 .\lab_1\teste_sms.py
```
