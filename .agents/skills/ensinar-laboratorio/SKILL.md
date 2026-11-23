---
name: ensinar-laboratorio
description: Ensina um laboratório do LLM-RedTeam-Labs por etapas, com leitura do código, demonstração local segura e avaliação de entendimento.
---

Use o catálogo em `docs/PROJECT-GUIDE.md` e leia o script selecionado. Comece pela finalidade, entradas, saídas e resultado esperado. Nas etapas seguintes, explique cada componente, o caminho pelo motor e as fronteiras de confiança.

Mostre a execução em PowerShell e explicite os pré-requisitos. Prefira demonstrações dos controles com respostas simuladas, sem rede, efeitos externos ou dados reais. Compare a hipótese e o resultado esperado com o que foi observado. Explique a falha em termos de permissões e decisões do código e apresente as defesas correspondentes.

Faça uma pergunta de compreensão e aguarde `next` antes de cada nova etapa.

## Comandos em PowerShell

Nos roteiros e demonstrações, defina `$labPython` com o caminho do executável do ambiente virtual usado pelo laboratório. Execute scripts, módulos e testes com `& $labPython`. Assim, a ativação por `Activate.ps1` é opcional. Se o roteiro for executado em outra janela, inclua novamente a definição da variável e indique a pasta de trabalho.

```powershell
# Exemplo do Lab 5, a partir da raiz do projeto
$labPython = '.\env\Scripts\python.exe'
& $labPython --version
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_rag_poisoning.py' -v
```
