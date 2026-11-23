# Histórico de sessões

## Lab 5 · RAG Poisoning e procedência

- Adicionado um índice fictício em memória e um catálogo de procedência. A implementação aprovada verifica ID e SHA-256 e cita o trecho recuperado. O cenário vulnerável está ilustrado no README por um fluxo conceitual.
- As três consultas do roteiro produziram os resultados esperados. Os quatro testes do Lab 5 e os três testes do motor passaram no Python 3.14.7. O diff dos Labs 1 a 4, do motor e de `requirements.txt` permaneceu vazio.
- O PowerShell bloqueou `Activate.ps1` pela política de execução. Os comandos foram validados apontando diretamente para `env/Scripts/python.exe`.

## 2026-11-22 · Auditoria e preparação

A auditoria começou na raiz Git, com a árvore de trabalho limpa em `main` e HEAD `308c999a5e4eaf97e936c96210760b06034540f6`. A comparação com a [página pública](https://github.com/paulinhoneto/LLM-RedTeam-Labs) cobriu a árvore exibida e o README renderizado.

### Achados confirmados

| Evidência | Efeito |
| --- | --- |
| `.venv/Scripts/python.exe` falhou por referenciar um Python 3.13 ausente. | O ambiente atual não inicia. A extensão binária de Pydantic presente também é identificada como CPython 3.13. |
| `requirements.txt` declara três pacotes sem versões. | Instalações podem resolver conjuntos diferentes. A auditoria leu os metadados locais e não avaliou atualizações ou advisories. |
| `motor_llm.py` inicializa FreeLLM fora do tratamento de exceções e converte falhas de chat em texto. | Falhas de inicialização impedem importação. Falhas de chat podem ser avaliadas como resposta normal e a mensagem bruta pode expor dados dependendo da exceção. A auditoria não observou exposição real. |
| Os labs 3 e 4 usam buscas de substrings para inferir intenção ou escolher uma ação simulada. | A avaliação não estabelece autorização e uma menção em texto pode ser confundida com uma ordem. Achado por inspeção do código. |
| O Lab 2 escolhe `chat:tools`, mas o motor não passa definições de ferramentas. No Lab 3, o console apenas imprime Markdown. | Esses scripts não validam execução estruturada de ferramentas ou efeitos de renderização. |
| O README aponta para `/issues` e o Lab 1 se anuncia como indireto. | A evidência está em `docs/` e o ponto de entrada do Lab 1 envia um pedido direto. |

### Verificações

- Python 3.14.7 em ambiente virtual temporário sem pip. Três testes `unittest` passaram com stubs para dotenv e FreeLLM. Cobertura de rota padrão, montagem de contexto, seletor de ferramentas e retorno de erro.
- Seis arquivos Python passaram na análise sintática. Os três arquivos de Skills passaram na checagem estrutural de nome, descrição e corpo. O validador oficial depende de PyYAML, ausente no ambiente de verificação. O carregamento das Skills pelo CLI não foi comprovado.
- Integração com dependências reais, roteamento de provedores e execução completa dos quatro scripts ficaram pendentes. O ambiente anterior está quebrado e a execução real pode usar credenciais e rede. O `.env` permaneceu sem leitura durante a auditoria.
