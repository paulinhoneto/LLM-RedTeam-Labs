# Roadmap

| Prioridade | Entrega | Verificação |
| --- | --- | --- |
| P0 | Recuperar o ambiente virtual, declarar versões de Python suportadas e tornar as dependências reproduzíveis | Instalação autorizada em ambiente limpo e suíte offline aprovada |
| P0 | Isolar inicialização e construção de mensagens do cliente FreeLLM, preservando `perguntar_ia()` | Mocks determinísticos e regressão dos argumentos e retornos existentes |
| P0 | Distinguir erro de resposta do modelo e ocultar detalhes sensíveis | Falha simulada registrada por categoria sem mensagem bruta, prompt ou chave |
| P1 | Verificar autorização antes de ações, validar argumentos e tratar texto e Markdown como dados | Testes de ações permitidas, negadas e saídas inertes |
| P1 | Automatizar sintaxe e suíte offline, mantendo `unittest` enquanto atender aos cenários | Verificações reproduzíveis no PowerShell e na CI. Considerar pytest para fixtures e parametrização quando houver ganho concreto |
| P2 | Ampliar catálogo por nível e criar um roteiro reutilizável para novos labs | Cada novo lab tem guia, fixtures e testes offline |
| P2 | Padronizar relatórios Red Team e Blue Team | Registrar escopo, hipótese, configuração, resultado esperado e observado, evidência, impacto, defesa e regressão |

## Cinco propostas de laboratório

| Nível | Laboratório | Resultado verificável |
| --- | --- | --- |
| Inicial | Fronteiras de confiança em entradas diretas e indiretas | Texto fornecido pelo usuário ou por um documento permanece classificado como dado |
| Intermediário | [Lab 5 · RAG poisoning e procedência](../lab_5/README.md) | Implementado. Documentos não aprovados ficam fora do contexto de um recuperador em memória |
| Intermediário | [Lab 6 · Tool Calling e autorização](../lab_6/README.md) | Implementado. Ações simuladas exigem permissão, titularidade e argumentos válidos |
| Intermediário | [Lab 7 · Segurança MCP](../lab_7/README.md) | Implementado. A resposta divulga o cartão somente após validar argumentos e escopo |
| Intermediário | [Lab 8 · Isolamento entre usuários](../lab_8/README.md) | Implementado. A leitura de notas fica restrita à conta da sessão |
| Avançado | Agente com ferramentas MCP simuladas | Operações em memória respeitam escopo, confirmação e limite de etapas |
| Avançado | [Lab 9 · Guardrails e avaliação](../lab_9/README.md) | Implementado. Mede bloqueios, falhas e falsos positivos com respostas fictícias |
| Intermediário | [Lab 10 · Consumo sem limites](../lab_10/README.md) | Implementado. Valida o tamanho da entrada e limita inferências simuladas por conta |
