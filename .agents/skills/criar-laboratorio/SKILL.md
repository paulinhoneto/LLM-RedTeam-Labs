---
name: criar-laboratorio
description: Planeja e implementa laboratórios defensivos reproduzíveis de segurança de LLMs para o catálogo do projeto.
---

Defina objetivo didático, nível, cenário, ativos fictícios, fronteiras de confiança, modelo de ameaça e hipótese verificável. Use exemplos conceituais de decisões inseguras e implemente a versão corrigida com controles verificáveis. Prefira fixtures, respostas determinísticas e operações em memória, sem rede ou ações reais.

Para cada novo laboratório, confira as pastas numeradas na raiz e use o número seguinte ao maior existente. Por exemplo, depois de `lab_9/`, crie `lab_10/`. Siga o modelo dos laboratórios recentes com script Python e `README.md` na nova pasta, testes em `tests/` e registro no catálogo.

Cubra com testes automatizados o uso legítimo e a rejeição de ações fora do escopo. Inclua README próprio com comandos PowerShell, roteiro didático e resultados esperados. Atualize o catálogo em `docs/PROJECT-GUIDE.md` e verifique a compatibilidade dos pontos de entrada existentes.

Consulte as propostas de injeção direta e indireta, RAG poisoning, Confused Deputy, autorização de ferramentas, agentes, MCP, vazamento fictício e avaliação de guardrails em `docs/ROADMAP.md`.
