# Tratamento de logs, CSV e JSON em Python

Versão documental **1.0.0** (11/11/2026). Código auditado `main` @ `b6d049208972ee62b6f7acc5c39b1e666776d392`; cenários não executados nesta revisão.

## Contexto e dependências
Python 3, bibliotecas csv, json, os, re e statistics; programas de console independentes.

## Módulos / contratos existentes
| Arquivo ou ação | Comportamento verificado no código | Cenário principal |
|---|---|---|
| `1/analise_logs.py` | Extrai tempos 'Execution Time: ...s' de log simulado de 10 épocas, calcula mean/stdev. | Testar 10 tempos; log sem match; apenas 1 tempo (stdev exige 2). |
| `2/escrever_csv.py` | Escreve ../dados_pessoais.csv com Nome, Idade e Cidade em UTF-8; registros de exemplo. | Testar existência, cabeçalho e 3 linhas, com diretório de trabalho controlado. |
| `3/ler_csv.py` | Lê o CSV escrito pelo exercício anterior usando DictReader e imprime 3 atributos. | Testar arquivo ausente, header inválido e ordem das linhas. |
| `4/manipular_json.py` | Escreve e lê dados_pessoa.json com nome, idade e cidade. | Testar ida e volta UTF-8; JSON corrompido; direitos do diretório. |

## Fluxo operacional
Os exemplos estão organizados para execução individual, sem backend próprio. Os scripts e suites têm efeitos e pré-condições diferentes: registrar o diretório de trabalho, dependência externa, dados usados e efeitos em arquivo/serviço.

```bash
python 1/analise_logs.py
```

## Riscos e decisões
Caminhos relativos dependem do diretório de execução; o CSV é gravado em ../, fora da pasta corrente. O log é literal no script e não lê logs reais. Os dados pessoais são amostras; não usar PII verdadeira em testes.

Esta documentação não cria infraestrutura, altera contrato nem valida automaticamente integração com a rede. Todo novo recurso requer caso de teste com dado de entrada, resultado esperado e evidência de execução.
