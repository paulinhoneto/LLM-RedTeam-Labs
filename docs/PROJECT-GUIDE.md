# Guia do projeto

## Arquitetura

Cada script é um ponto de entrada independente. Os Labs 1 a 4 adicionam a raiz ao caminho de importação e usam `motor_llm.perguntar_ia()`. O motor carrega o `.env` da raiz e cria o cliente FreeLLM durante a importação. A função recebe tarefa, contexto opcional e uma opção de roteamento. No modo `auto`, inclui uma mensagem de sistema sobre idioma. Em `chat:tools`, omite essa mensagem. O contexto, quando presente, e a tarefa são mensagens de usuário distintas. O motor passa apenas as mensagens e o seletor de modelo a `chat()`. A função retorna o texto do modelo ou uma mensagem textual de erro.

O Lab 3 usa uma leitura simulada e uma função de e-mail que imprime no console. O Lab 4 também simula a ação em console. O Lab 2 seleciona um modelo com capacidade de ferramentas, mas a integração atual não registra ferramentas nem processa chamadas estruturadas. O Lab 3 imprime Markdown como texto no terminal.

## Catálogo

| Lab | Nível sugerido | Entrada e saída |
| --- | --- | --- |
| 1 · Injeção direta | Inicial | Pedido textual com caso de reversão → resposta do modelo no console |
| 2 · Injeção indireta | Intermediário | Tarefa e log fictício apresentado como resultado de ferramenta → resposta no console |
| 3 · Injeção em cadeia e Markdown | Intermediário | Tarefa e backup simulado → resposta e avaliação heurística no console |
| 4 · Confused Deputy | Avançado | Tarefa e SMS fictício → resposta do modelo e decisão simulada do orquestrador |
| [5 · RAG Poisoning e procedência](../lab_5/README.md) | Intermediário | Consulta ao acervo fictício → trechos aprovados com indicação de fonte |
| [6 · Tool Calling e autorização](../lab_6/README.md) | Intermediário | Proposta de ação e sessão simulada → decisão e estado de um chamado fictício |
| [7 · Segurança MCP](../lab_7/README.md) | Intermediário | Mensagem `tools/call` e escopo da sessão → resultado autorizado ou erro |
| [8 · Isolamento entre usuários](../lab_8/README.md) | Intermediário | Sessão fictícia e ID da nota → conteúdo da conta ou indicação de indisponibilidade |
| [9 · Guardrails e avaliação](../lab_9/README.md) | Avançado | Respostas fictícias rotuladas → matriz de resultados e taxas de erro por filtro |
| [10 · Consumo sem limites](../lab_10/README.md) | Intermediário | Solicitações fictícias → decisão por tamanho e cota por conta |

Os onze relatórios `issue_lab_*.txt` estão em [docs](./) e registram experimentos históricos. O [README principal](../README.md) reúne o catálogo e o início rápido. O Lab 1 atual envia um pedido direto sem contexto, embora o banner diga “indireta”. Os cenários históricos de Base64 estão nos relatórios.

## Execução em PowerShell

Execute a partir da raiz. A base atual declara `freelm`, `python-dotenv` e `groq` sem versões fixadas. Os metadados do ambiente antigo registram respectivamente **0.5.2**, **1.2.4** e **1.7.0**. A compatibilidade da instalação com Python 3.14 está pendente. Use um interpretador funcional e um novo ambiente, pois o `.venv` existente referencia uma instalação Python 3.13 ausente.

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

O caminho do interpretador pode ser usado diretamente caso o alias `python` aponte para a Microsoft Store. O diretório `venv/` é ignorado pelo Git e permite preservar o ambiente antigo. Instalação e integração com provedores devem ocorrer com autorização. Para integração autorizada configure a chave do provedor no `.env` da raiz, por exemplo com a variável `GROQ_API_KEY`. O Git ignora esse arquivo.

Cada comando abaixo é um ponto de entrada que pode chamar um provedor externo. Use dados fictícios e execute apenas dentro de um escopo autorizado.

```powershell
.\venv\Scripts\python.exe .\lab_1\teste_sms.py
.\venv\Scripts\python.exe .\lab_2\teste_injecao_indireta.py
.\venv\Scripts\python.exe .\lab_3\teste_chained_injection.py
.\venv\Scripts\python.exe .\lab_4\teste_confused_deputy.py
```

O [Lab 5](../lab_5/README.md) funciona com a biblioteca padrão, usando um índice simulado em memória e um catálogo aprovado separado. Seu README contém os passos para criar e ativar o ambiente e enviar as consultas.

O [Lab 6](../lab_6/README.md) também funciona offline. Seu README inclui o preparo do ambiente e três cenários que comparam permissão e titularidade.

O [Lab 7](../lab_7/README.md) simula o tratamento de mensagens `tools/call` e verifica argumentos e permissões antes de retornar um cartão fictício.

O [Lab 8](../lab_8/README.md) demonstra consultas em memória limitadas à conta da sessão, inclusive quando duas contas usam o mesmo ID.

O [Lab 9](../lab_9/README.md) compara dois filtros de saída com respostas fixas e mede falhas e bloqueios indevidos.

O [Lab 10](../lab_10/README.md) demonstra como validar o tamanho da entrada e aplicar uma cota por conta antes da inferência simulada.

Para verificar o motor e os Labs 5 a 10 localmente, execute o comando abaixo. A suíte usa apenas a biblioteca padrão e, nos testes do motor, simula o carregamento do ambiente e a chamada do provedor.

```powershell
.\venv\Scripts\python.exe -I -B -m unittest discover -s tests -v
```
