# Instruções do projeto

- Comunique-se e documente em português brasileiro. Use nomes de funções, classes e variáveis em inglês ao criar ou refatorar código Python. Preserve as interfaces e os pontos de entrada existentes, incluindo `perguntar_ia()`. Evite renomeações cosméticas nos laboratórios.
- Prefira PowerShell no Windows e execute Python em ambiente virtual. Peça autorização antes de instalar dependências, usar serviços pagos ou realizar operações destrutivas.
- Preserve o trabalho local. Proteja credenciais, tokens, arquivos `.env` e dados sensíveis. Use valores fictícios em exemplos e elimine dados sensíveis dos logs, testes e relatórios.
- Cubra funcionalidades novas com testes automatizados. Prefira respostas determinísticas e dependências simuladas para testes sem rede. Documente alterações arquiteturais e impactos de compatibilidade.
- Distinga hipótese, comportamento demonstrado localmente com dados fictícios e vulnerabilidade comprovada dentro do escopo aprovado.
- Restrinja operações de segurança a recursos locais, próprios ou expressamente autorizados. Testes em serviços externos exigem autorização prévia e definição de escopo.
- No modo instrutor, apresente uma etapa didática por vez, avalie o entendimento e aguarde `next`. No modo engenheiro, avance autonomamente nas tarefas locais autorizadas e verifique os resultados.

## Prompts para iniciar uma iteração

Quando o usuário digitar `prompts`, mostre os títulos e uma descrição curta das opções numeradas abaixo e aguarde a escolha. Aceite o número sozinho ou acompanhado de contexto, como `2 — validação de saída`, `4 — lab_8` ou `5 — motor_llm.py`. Se o usuário já tiver dado contexto suficiente, comece pela opção escolhida.

1. **ENTENDER O MOTOR LLM** — Use `ensinar-laboratorio`. Percorra `motor_llm.py` do prompt até a resposta. Explique as mensagens enviadas, a configuração da chamada e o retorno ao laboratório. Use uma etapa por vez e aguarde `next`.
2. **CRIAR O PRÓXIMO LABORATÓRIO** — Use `criar-laboratorio`. Use o tema fornecido ou escolha um tema da OWASP Top 10 para aplicações com LLMs que complemente o catálogo. Implemente o laboratório defensivo com dados fictícios, README, comandos PowerShell e testes offline. Atualize o catálogo e informe o que foi verificado.
3. **MONTAR UM ROTEIRO DE ESTUDOS** — Leia o catálogo e proponha uma sequência por pré-requisitos. Para cada laboratório, indique o conceito a estudar, a prática a executar e o resultado que o usuário deve conseguir explicar ou demonstrar.
4. **ESTUDAR UM LABORATÓRIO** — Use `ensinar-laboratorio`. Explique o objetivo, as entradas, o código, o controle defensivo e o que cada teste comprova. Demonstre a execução local com `& $labPython` quando possível. Faça uma checagem de entendimento e aguarde `next` entre etapas. Se nenhum laboratório for indicado, peça o número mostrando o catálogo.
5. **REVISAR A SEGURANÇA DO PROJETO** — Use `revisar-seguranca`. Revise o arquivo, laboratório ou controle indicado. Se a escolha vier sem escopo, comece pelo motor compartilhado. Apresente evidências, impacto e recomendações priorizadas. Mantenha esta opção como revisão e faça alterações no código quando o usuário pedir.

Ao escolher a opção 2 para criar um laboratório, verifique na raiz o maior número entre as pastas `lab_N` e crie `lab_<maior + 1>` em minúsculas. Por exemplo, com `lab_1/` a `lab_9/`, crie `lab_10/`. Siga a estrutura dos laboratórios recentes e preserve as pastas anteriores.
