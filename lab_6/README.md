# Lab 6 · Tool Calling e autorização

**Nível intermediário.** Tool calling permite ao modelo propor uma chamada estruturada com o nome da ferramenta e seus argumentos. A aplicação recebe essa proposta e decide se pode executá-la.

## Cenário e hipótese

Ana é titular do chamado fictício `CH-01`. A ferramenta `close_ticket` muda seu estado de `aberto` para `fechado`, em memória. O ativo protegido é o estado do chamado. O risco é uma proposta válida para um chamado que o solicitante não pode alterar.

No desenho inseguro, a aplicação confunde uma proposta bem formada com autorização. Mesmo uma chamada estruturalmente válida pode atuar fora do escopo do solicitante. Esse cenário é conceitual.

Na implementação executável, o controlador aceita somente `close_ticket`, valida o argumento `ticket_id` e verifica a permissão e a titularidade no código. A identidade e a permissão vêm de fixtures que representam a sessão autenticada. O argumento `--cenario` escolhe a fixture para a demonstração. Em uma aplicação real, esses dados viriam da sessão autenticada no servidor. A proposta da ferramenta é fixa nos três cenários.

**Hipótese verificável** · A mesma proposta deixa o chamado fechado somente quando o solicitante é titular e possui a permissão de fechamento. Cada execução começa com um chamado aberto.

## Demonstração em PowerShell

Abra outra janela e cole este bloco para usar o ambiente virtual do projeto. O Lab 6 usa apenas a biblioteca padrão e funciona offline.

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

Execute os casos e compare as linhas `Antes` e `Depois`.

```powershell
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario autorizado
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario outro-titular
& $labPython -I -B -X utf8 .\lab_6\tool_calling.py --cenario sem-permissao
```

| Cenário | Sessão simulada | Decisão esperada | Estado final |
| --- | --- | --- | --- |
| `autorizado` | Ana tem a permissão | Permitido | Fechado |
| `outro-titular` | Bruno tem a permissão, mas o chamado é de Ana | Negado | Aberto |
| `sem-permissao` | Ana é titular, mas não tem a permissão | Negado | Aberto |

## Testes

```powershell
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_tool_calling.py' -v
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

Os seis testes do Lab 6 verificam o fechamento permitido e a preservação do estado ao negar outro titular, falta de permissão, ferramenta desconhecida, argumentos inválidos ou chamado inexistente.

**Checagem de entendimento** · A proposta é igual nos três cenários. Por que Bruno não consegue fechar o chamado mesmo tendo permissão para usar a ferramenta?
