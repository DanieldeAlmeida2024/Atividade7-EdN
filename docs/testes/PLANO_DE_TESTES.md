# Plano de testes — Atividade7-EdN

Versão documental **1.0.0** (11/11/2026). Código auditado `main` @ `b6d049208972ee62b6f7acc5c39b1e666776d392`; cenários não executados nesta revisão.

## Matriz vinculada ao código
| ID | Artefato | Critério verificável | Situação |
|---|---|---|---|
| T-01 | `1/analise_logs.py` | Testar 10 tempos; log sem match; apenas 1 tempo (stdev exige 2). | Planejado/requer execução |
| T-02 | `2/escrever_csv.py` | Testar existência, cabeçalho e 3 linhas, com diretório de trabalho controlado. | Planejado/requer execução |
| T-03 | `3/ler_csv.py` | Testar arquivo ausente, header inválido e ordem das linhas. | Planejado/requer execução |
| T-04 | `4/manipular_json.py` | Testar ida e volta UTF-8; JSON corrompido; direitos do diretório. | Planejado/requer execução |

## Cenários adicionais e regressão
- N-01: ausência do arquivo/serviço necessário; mensagem controlada ou erro capturado.
- N-02: resposta/conteúdo fora do contrato (schema e tipos); não marcar como aprovado por mera presença de arquivo.
- N-03: dados incorretos e entradas vazias; não sobrescrever arquivos do usuário ou produzir mutações não solicitadas.
- N-04: repetir a execução em ambiente limpo e comparar evidências.

## Execução
```bash
python 1/analise_logs.py
```

Registrar SHA, versão da ferramenta, fixtures, resultado, stdout/HTTP, condições de rede e duração. `tests/test_documentacao.py` é apenas verificação documental; não substitui os cenários acima.
