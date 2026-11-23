# Lab 9 · Guardrails e avaliação

**Português (Brasil)** · [English](README.en.md)

**Nível avançado.** Compare dois filtros de saída usando as mesmas seis respostas fictícias. A pergunta de avaliação é quantas saídas indevidas passam e quantas legítimas são bloqueadas.

## Cenário e hipótese

Um assistente fictício pode receber dados públicos e dados privados. A fronteira exercitada aqui fica entre a resposta produzida e o texto exibido ao usuário. A política do exercício bloqueia referências privadas e informações de agenda privada, enquanto permite informações públicas e respostas sem dados. Cada caso tem um rótulo esperado definido previamente. O simulador fornece respostas fixas, sem LLM, rede ou credenciais.

O filtro de referência bloqueia por uma palavra genérica. O segundo reconhece o formato de um marcador fictício usado nas referências privadas. A hipótese é que a regra específica reduz ambos os tipos de erro nessa amostra. O filtro de marcador só cobre esse tipo de referência. A política também inclui agenda privada, o que deixa uma falha visível na avaliação.

| Sigla | Significado |
| --- | --- |
| VP | Saída indevida bloqueada |
| FN | Saída indevida que passou |
| FP | Saída legítima bloqueada |
| VN | Saída legítima que passou |

A taxa de bloqueio de indevidas é VP dividido pelo total de casos indevidos. A taxa de falhas é FN dividido pelo mesmo total. A taxa de falsos positivos é FP dividido pelo total de casos legítimos. Para um grupo vazio, o relatório exibe `n/a`.

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
& $labPython -I -B -X utf8 .\lab_9\guardrail_evaluation.py --filtro comparar
```

Para executar um filtro individualmente, use `--filtro palavra` ou `--filtro marcador`. O relatório exibe os resultados por caso e as taxas agregadas.

| Filtro | VP | FN | FP | VN | Bloqueio de indevidas | Falhas | Falsos positivos |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Palavra | 1 | 2 | 1 | 2 | 1/3 | 2/3 | 1/3 |
| Marcador | 2 | 1 | 0 | 3 | 2/3 | 1/3 | 0/3 |

## Roteiro didático

1. Compare o caso `manual-publico` nos dois relatórios. O bloqueio indevido aparece como FP no primeiro.
2. Encontre `agenda-privada` e explique por que ela continua como FN. O filtro reconhece referências privadas padronizadas; a regra da aplicação é mais ampla.
3. Calcule a taxa de falhas usando o total de respostas indevidas como denominador. As taxas descrevem os seis casos do exercício. Elas não estimam o desempenho de um modelo ou uma implantação real.

## Testes

```powershell
& $labPython -I -B -X utf8 -m unittest discover -s tests -p 'test_guardrail_evaluation.py' -v
& $labPython -I -B -X utf8 -m unittest discover -s tests -v
```

**Checagem de entendimento** · Se o filtro deixa passar uma de três respostas indevidas, qual é a taxa de falhas? O que você precisaria medir para saber se ele também bloqueia respostas legítimas?
