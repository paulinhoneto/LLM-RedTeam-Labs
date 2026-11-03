\# 🛡️ LLM RedTeam Labs



\*\*Framework de Pesquisa e Testes de Segurança (Red Team) em Large Language Models.\*\*



Este repositório contém uma suíte de laboratórios práticos desenvolvidos para explorar, validar e documentar vulnerabilidades em sistemas baseados em Inteligência Artificial, seguindo as diretrizes do OWASP Top 10 para LLMs.



\## 🎯 Objetivos do Projeto

O foco principal é demonstrar, através de provas de conceito (PoCs) em Python, como as falhas de segurança em IA muitas vezes não estão no modelo em si (que possui alinhamento RLHF), mas sim na arquitetura do \*\*Orquestrador\*\* (o código que conecta a IA às ferramentas e dados).



\## 🧪 Laboratórios Incluídos



\- \*\*Lab 1: Injeção Direta e Jailbreak\*\* - Testes de bypass de guardrails usando engenharia social, inversão de strings e codificação (Base64).

\- \*\*Lab 2: Injeção Indireta (Context Poisoning)\*\* - Exploração de falhas através da inserção de comandos maliciosos em contextos (SMS, e-mails, logs).

\- \*\*Lab 3: Chained Injection \& Markdown\*\* - Tentativas de exfiltração de dados usando injeções em cadeia e renderização de links/imagens maliciosas.

\- \*\*Lab 4: Confused Deputy (Falha de Orquestração)\*\* - Demonstração de como um Orquestrador frágil pode executar ações maliciosas ao confiar cegamente na saída (output) do LLM.



\## 🛠️ Tecnologias Utilizadas

\- \*\*Python 3\*\*

\- \*\*freelm\*\* (Roteamento dinâmico de APIs gratuitas: Groq, Gemini, OpenRouter)

\- \*\*python-dotenv\*\* (Gerenciamento de credenciais)



\## ⚙️ Como Executar

1\. Clone o repositório.

2\. Crie um ambiente virtual (`python -m venv .venv`) e ative-o.

3\. Instale as dependências (`pip install -r requirements.txt`).

4\. Crie um arquivo `.env` na raiz com as suas chaves de API (ex: `GROQ\_API\_KEY="sua\_chave"`).

5\. Navegue até a pasta do laboratório desejado e execute o script (ex: `python lab\_1/teste\_sms.py`).



\## 📄 Documentação

Os resultados e análises de cada teste estão documentados na pasta de relatórios (`/issues`), contendo a visão do atacante (Red Team) e as mitigações recomendadas (Blue Team).



\---

\*Este projeto foi desenvolvido para fins estritamente educacionais e de pesquisa em segurança cibernética.\*

