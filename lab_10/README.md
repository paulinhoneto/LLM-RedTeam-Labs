# Lab 10 · Consumo sem limites

**Nível intermediário.** Verifique como um serviço pode proteger a capacidade de inferência com limites aplicados antes da chamada ao modelo. O tema corresponde a [Consumo sem limites no OWASP Top 10 de 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/).

## Cenário e hipótese

Ana e Bruno usam um assistente fictício. O recurso protegido é a capacidade de chamar o modelo. No desenho inseguro, toda solicitação consome uma chamada sem validação de tamanho nem cota. A implementação executável rejeita entradas vazias ou acima de 40 caracteres e limita cada conta a duas chamadas por execução.

**Hipótese** · Requisições rejeitadas não chegam ao modelo e uma conta que esgota sua cota não consome a cota de outra. O ID da conta é fornecido pelo cenário como dado da aplicação. Em um serviço, esse ID viria da sessão autenticada.

O modelo é uma função simulada, e o contador existe somente na memória do processo. O limite conta caracteres Python, uma medida didática distinta da contagem de tokens. Uma chamada autorizada reserva a cota antes de chamar o modelo, porque uma tentativa pode consumir capacidade mesmo se falhar.

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
& $labPython -I -B -X utf8 .\lab_10\resource_limits.py
```

| Solicitação | Resultado esperado |
| --- | --- |
| Primeira de Ana | Modelo simulado chamado |
| Entrada acima do limite | Rejeitada antes de chamar o modelo |
| Segunda solicitação válida de Ana | Modelo simulado chamado |
| Terceira solicitação válida de Ana | Cota esgotada |
| Solicitação de Bruno | Modelo simulado chamado |

O contador final deve mostrar **três chamadas**. O roteiro usa dados fixos, sem rede, dependências externas ou custos de API.

## Testes e roteiro didático

```powershell
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_resource_limits.py' -v
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

1. Observe que a entrada acima do limite foi rejeitada e Ana ainda conseguiu fazer sua segunda inferência.
2. Compare a resposta da terceira solicitação válida de Ana com a resposta de Bruno.
3. Leia os testes e encontre a asserção que confirma que entradas inválidas não acionam o modelo.

**Checagem de entendimento** · Foram processadas cinco solicitações pela aplicação. Por que o contador do modelo mostra três?
