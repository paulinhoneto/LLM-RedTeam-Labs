# Lab 8 · Isolamento entre usuários

**Português (Brasil)** · [English](README.en.md)

**Nível intermediário.** Use duas contas fictícias para verificar que uma consulta só retorna dados da conta associada à sessão.

## Cenário e hipótese

Ana e Bruno têm notas privadas, guardadas em memória. Os dois têm uma nota com o ID `NOTA-01`, com textos distintos. Somente Bruno tem a `NOTA-02`.

O desenho inseguro é uma busca global que usa apenas o ID da nota. O ID informa **qual nota** foi pedida, enquanto a sessão determina **em qual conta** a busca pode ocorrer. Mesmo um ID que existe no sistema pode estar fora do escopo do solicitante.

A implementação consulta primeiro o conjunto de notas da conta da sessão e só então busca o ID. A hipótese é que o mesmo ID retorna conteúdos diferentes para contas diferentes e que uma nota exclusiva de Bruno fica indisponível na sessão de Ana. A saída de uma nota fora do escopo é igual à de uma nota inexistente.

O comando `--sessao` seleciona uma fixture de teste que representa uma sessão autenticada. Em produção, o servidor deve obter a conta da sessão autenticada. O laboratório simula apenas a consulta de dados em memória, sem login real, LLM ou rede.

## Execute no PowerShell

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

O laboratório usa apenas a biblioteca padrão. Execute os casos e compare as respostas.

```powershell
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao ana --nota NOTA-01
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao bruno --nota NOTA-01
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao bruno --nota NOTA-02
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao ana --nota NOTA-02
& $labPython -I -B -X utf8 .\lab_8\user_isolation.py --sessao ana --nota NOTA-99
```

| Sessão | Nota | Saída esperada |
| --- | --- | --- |
| Ana | `NOTA-01` | Ana: revisar o catálogo. |
| Bruno | `NOTA-01` | Bruno: organizar a agenda. |
| Bruno | `NOTA-02` | Bruno: preparar o relatório. |
| Ana | `NOTA-02` | Nota indisponível nesta sessão. |
| Ana | `NOTA-99` | Nota indisponível nesta sessão. |

## Testes

```powershell
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_user_isolation.py' -v
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

Os quatro testes verificam IDs iguais em contas diferentes, acesso exclusivo do titular, ausência de acesso para uma conta desconhecida e mensagens idênticas no console para notas fora do escopo e inexistentes.

**Checagem de entendimento** · Qual informação além do ID permite que o sistema escolha a nota certa quando Ana e Bruno pedem `NOTA-01`?
