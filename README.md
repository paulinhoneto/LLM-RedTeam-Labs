# LLM-RedTeam-Labs

Laboratórios em Python para estudar segurança de aplicações com modelos de linguagem (LLMs). O projeto mostra onde o código que conecta o modelo a dados e ferramentas pode aplicar controles de procedência, autorização, isolamento e limites de uso. Os exercícios usam dados fictícios e abordam temas do OWASP Top 10 para aplicações com LLMs.

## Comece offline pelo PowerShell

Na raiz do repositório, use um Python instalado para criar um ambiente virtual. Se `env` já existir e estiver funcional, basta definir `$labPython` e executar os dois últimos comandos.

```powershell
python -m venv --without-pip .\env
$labPython = '.\env\Scripts\python.exe'
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario outro-titular
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

No Lab 6, o chamado permanece aberto quando a proposta parte de uma sessão sem acesso àquele recurso. Os Labs 5 a 10 e a suíte de testes usam a biblioteca padrão, sem chamadas de rede ou configuração de credenciais. Os testes do motor usam um cliente simulado.

## Catálogo de laboratórios

| Lab | Tema | O que observar |
| --- | --- | --- |
| [1](lab_1/teste_sms.py) | Injeção direta | O script envia um pedido de transformação de texto como mensagem do usuário. |
| [2](lab_2/teste_injecao_indireta.py) | Injeção indireta | O script apresenta ao modelo um log fictício como contexto. |
| [3](lab_3/teste_chained_injection.py) | Injeção em cadeia e Markdown | O orquestrador avalia texto e simula uma ação no console. |
| [4](lab_4/teste_confused_deputy.py) | Confused Deputy | O exemplo ilustra o risco de decidir uma ação com base no texto do modelo. |
| [5](lab_5/README.md) | RAG Poisoning | A recuperação omite documentos que não correspondem ao catálogo aprovado. |
| [6](lab_6/README.md) | Tool Calling | A mesma proposta tem resultados diferentes conforme a permissão e a titularidade. |
| [7](lab_7/README.md) | Segurança MCP | Uma chamada simulada passa por validação de entrada e verificação de escopo. |
| [8](lab_8/README.md) | Isolamento entre usuários | A resolução do ID de uma nota depende da conta da sessão. |
| [9](lab_9/README.md) | Guardrails e avaliação | Filtragens de saída são comparadas por falsos positivos e falsos negativos. |
| [10](lab_10/README.md) | Consumo sem limites | Entradas inválidas e contas sem cota são barradas antes da inferência simulada. |

## Labs 1 a 4 com provedor

Os quatro scripts usam [`motor_llm.py`](motor_llm.py), que monta as mensagens e chama o provedor via FreeLLM. Para executá-los em um escopo autorizado, prepare um ambiente separado com pip e as dependências de [`requirements.txt`](requirements.txt).

```powershell
python -m venv .\venv
$labPython = '.\venv\Scripts\python.exe'
& $labPython -m pip install -r .\requirements.txt
```

Configure localmente a variável do provedor no `.env` da raiz, como `GROQ_API_KEY` para Groq. O Git ignora esse arquivo. Execute o script do laboratório desejado a partir da raiz, por exemplo `& $labPython -I -B -X utf8 .\lab_1\teste_sms.py`. O [guia do projeto](docs/PROJECT-GUIDE.md) traz os comandos dos quatro laboratórios e os detalhes do motor.

## Documentação

- [Guia do projeto](docs/PROJECT-GUIDE.md) para arquitetura e execução.
- [Relatórios históricos](docs/) para observações de experimentos anteriores e propostas de mitigação.
- [Roadmap](docs/ROADMAP.md) e [histórico de sessões](docs/SESSION-LOG.md) para acompanhar a evolução do projeto.
- [Instruções do projeto](AGENTS.md) para usar o menu `prompts` no Codex e escolher entre estudo, criação de laboratórios e revisão de segurança.

Use dados fictícios e mantenha os exercícios em recursos locais, próprios ou expressamente autorizados. Ao registrar resultados, indique se a evidência vem de uma simulação local ou de uma chamada real ao provedor.
