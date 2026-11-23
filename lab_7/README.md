# Lab 7 · Segurança MCP

**Português (Brasil)** · [English](README.en.md)

**Nível intermediário.** Aprenda a validar argumentos e verificar permissões em cada chamada de ferramenta. O laboratório simula, em memória, a fronteira do servidor que recebe uma mensagem `tools/call`. Ele usa o formato de mensagem da [especificação MCP](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) e cobre apenas esse recorte, sem transporte, negociação de sessão ou SDK.

## Cenário e hipótese

Um cliente pede à ferramenta `read_card` para ler um cartão fictício. A mensagem contém o identificador do cartão. O servidor recebe, separadamente, o conjunto de cartões que a sessão pode consultar. Na demonstração, esse conjunto vem de uma fixture. Em uma integração real, ele seria derivado da identidade autenticada e da política de acesso.

No desenho inseguro, o servidor devolve o cartão assim que o identificador tem um formato válido. A vulnerabilidade conceitual é confundir **entrada válida** com **permissão para ler um recurso**. O ativo protegido é o conteúdo do cartão.

A implementação verifica o envelope JSON-RPC, o método e o nome da ferramenta. Em seguida exige somente `card_id`, do tipo texto e no formato `CARD-000`. Por fim, confere se o cartão está no escopo da sessão antes de retornar conteúdo. Cartões ausentes ou fora do escopo recebem a mesma mensagem de negação.

**Hipótese verificável** · Uma chamada com identificador válido só retorna conteúdo se o cartão existir e a sessão tiver acesso. Erros de entrada e de autorização retornam `result.isError: true`. Erros de protocolo retornam `error`.

## Execute no PowerShell

Abra uma janela nova e selecione o Python do ambiente. O laboratório usa apenas a biblioteca padrão.

```powershell
Set-Location 'C:\Users\vanin\Documents\IA'
$labPython = '.\env\Scripts\python.exe'
if (-not (Test-Path $labPython)) {
    $pythonBase = Join-Path $env:LOCALAPPDATA 'Python\pythoncore-3.14-64\python.exe'
    & $pythonBase -m venv --without-pip .\env
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar o ambiente virtual.' }
}
& $labPython --version
```

Os cenários geram mensagens fixas. Compare os campos `isError` e `content` do JSON impresso.

```powershell
& $labPython -I -B -X utf8 .\lab_7\mcp_security.py --cenario autorizado
& $labPython -I -B -X utf8 .\lab_7\mcp_security.py --cenario entrada-invalida
& $labPython -I -B -X utf8 .\lab_7\mcp_security.py --cenario sem-permissao
```

| Cenário | Entrada e sessão | Resultado esperado |
| --- | --- | --- |
| `autorizado` | `CARD-001`, dentro do escopo | `isError: false`, texto do cartão |
| `entrada-invalida` | ID vazio, sessão com acesso ao cartão | `isError: true`, formato inválido |
| `sem-permissao` | `CARD-001`, sessão sem acesso | `isError: true`, acesso negado sem revelar o conteúdo |

## Testes

```powershell
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_mcp_security.py' -v
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

Os testes cobrem leitura autorizada, negação sem expor conteúdo, argumentos inválidos, ferramenta desconhecida, método desconhecido e envelope inválido.

**Checagem de entendimento** · Nos cenários `autorizado` e `sem-permissao`, o cliente envia o mesmo ID. O que muda na decisão do servidor?
