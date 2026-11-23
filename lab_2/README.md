# Lab 2 · Injeção indireta

**Português (Brasil)** · [English](README.en.md) · [Catálogo](../README.md)

O script envia uma tarefa e um log fictício separado ao modelo. O console mostra o texto retornado. O script seleciona uma rota com capacidade de ferramentas, sem registrar ferramentas para execução.

## Execute no PowerShell

A partir da raiz, use o ambiente preparado na seção [Labs 1 a 4 com provedor](../README.md#labs-1-a-4-com-provedor). O resultado depende do provedor configurado. Use dados fictícios e escopo autorizado.

```powershell
& $labPython -I -B -X utf8 .\lab_2\teste_injecao_indireta.py
```
