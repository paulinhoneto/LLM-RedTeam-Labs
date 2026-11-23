# Lab 5 · RAG Poisoning e procedência

**Português (Brasil)** · [English](README.en.md)

**Nível intermediário.** Em RAG (geração aumentada por recuperação), um sistema busca documentos e fornece os trechos encontrados como contexto para a resposta. Neste exercício, um acervo fictício em memória representa o índice e a saída cita os trechos aprovados diretamente. Isso torna visível a seleção de contexto sem depender de um modelo.

## Cenário e modelo de ameaça

Vila Aurora tem um registro oficial para a biblioteca e outro para o museu. A fonte oficial informa que a biblioteca fecha às 18h, enquanto um rascunho não aprovado informa 23h. O ativo protegido é a integridade do contexto. A busca retorna candidatos de um índice misto, enquanto o mantenedor controla separadamente o catálogo de documentos aprovados.

### Exemplo vulnerável conceitual

```text
Pergunta → busca por relevância → candidatos → contexto
                                               ├─ horário oficial: 18h
                                               └─ rascunho: 23h
```

Nesse desenho, os dois trechos podem chegar juntos ao gerador. Uma possível consequência é uma resposta que reproduza o horário incorreto. O diagrama representa a falha de projeto e a consequência é uma hipótese sobre a etapa de geração.

### Implementação corrigida

```text
Pergunta → candidatos → validação de ID e SHA-256 → seleção por termos → trechos citados
                               ↑
                      catálogo aprovado
```

`rag_poisoning.py` confere se o identificador e o hash do conteúdo correspondem ao catálogo aprovado antes de selecionar trechos para a consulta. A hipótese verificável é que o horário oficial permanece na saída quando um candidato não aprovado também está disponível. Um conteúdo divergente que reutiliza um ID oficial também é descartado. O hash vincula o conteúdo ao registro confiável. O exercício pressupõe que o catálogo está protegido e usa correspondência simples por palavras, sem embeddings.

## Execute em outra janela do PowerShell

### 1. Abra o projeto e crie o ambiente

Use Python 3.14.7, verificado nesta máquina. O caminho abaixo usa o executável funcional encontrado durante a auditoria. Em outra máquina, ajuste `$pythonBase` para o caminho de um Python instalado.

```powershell
Set-Location 'C:\Users\vanin\Documents\IA'
$pythonBase = Join-Path $env:LOCALAPPDATA 'Python\pythoncore-3.14-64\python.exe'
& $pythonBase --version
if (-not (Test-Path .\env\Scripts\python.exe)) {
    & $pythonBase -m venv --without-pip .\env
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar o ambiente virtual.' }
}
```

### 2. Ative o ambiente

```powershell
. .\env\Scripts\Activate.ps1
python --version
```

Se a política do PowerShell bloquear a ativação, execute os comandos das próximas etapas trocando `python` por `& .\env\Scripts\python.exe`. O Lab 5 usa apenas a biblioteca padrão e funciona sem instalar dependências ou configurar o `.env`.

### 3. Envie as consultas

Os prompts são passados diretamente ao script em `--pergunta`.

```powershell
python -I -B -X utf8 .\lab_5\rag_poisoning.py --pergunta "Qual é o horário da biblioteca?"
python -I -B -X utf8 .\lab_5\rag_poisoning.py --pergunta "Horário do museu?"
python -I -B -X utf8 .\lab_5\rag_poisoning.py --pergunta "Onde fica a farmácia?"
```

| Consulta   | Saída esperada                                                   |
| -----------|------------------------------------------------------------------|
| Biblioteca | `[oficial-biblioteca] A biblioteca da Vila Aurora fecha às 18h.` |
| Museu      | `[oficial-museu] O museu da Vila Aurora abre às 10h.`            |
| Farmácia   | `Nenhuma fonte aprovada corresponde à pergunta.`                 |

### 4. Rode os testes e encerre

```powershell
python -I -B -X utf8 -m unittest discover -s tests -p 'test_rag_poisoning.py' -v
python -I -B -X utf8 -m unittest discover -s tests -v
deactivate
```

A primeira execução roda os quatro testes deste laboratório. A segunda inclui também os três testes do motor. Use `deactivate` se tiver ativado o ambiente.

## Roteiro didático

1. Compare o horário da fonte oficial com o do rascunho no cenário conceitual.
2. Execute a consulta sobre a biblioteca e identifique a fonte citada.
3. Execute as consultas sobre o museu e a farmácia para comparar uma recuperação válida com a ausência de evidência.
4. Leia `retrieve()` e encontre a condição que valida a procedência. Depois localize o teste que verifica a preservação da versão oficial quando o conteúdo de um candidato diverge.

**Checagem de entendimento** · O que ainda poderia dar errado se a aplicação confiasse apenas no ID do documento? Qual parte da implementação verifica também o conteúdo?
