# Plano de testes — Atividade 07

Versão 1.1.0 — 14/11/2026

Comando: `python -m unittest discover -s tests -p 'test_*.py' -v`.

| ID | Componente | Entrada / condição | Esperado |
| --- | --- | --- | --- |
| LOG-01 | Análise | Amostra com 10 épocas | Dez tempos, média válida, desvio positivo |
| LOG-02 | Análise | Uma época `12.3s` | Média 12.3, desvio 0 |
| LOG-03 | Análise | Log sem tempos | `ValueError` explícito |
| CSV-01 | Escrita/leitura | Três registros fictícios | Roundtrip sem perda de acentos |
| CSV-02 | Leitura | Cabeçalho ausente/errado | Erro de validação |
| CSV-03 | Leitura | Idade negativa, texto, linha incompleta | Erro com número da linha |
| JSON-01 | Escrita/leitura | Unicode, idade válida | Roundtrip preservado |
| JSON-02 | Leitura | JSON malformado, faltam campos, idade booleana | Rejeitado |
| CLI-01 | CSV | Execução com cwd diferente da raiz | Arquivo escrito e lido no caminho solicitado |
| CLI-02 | Logs | Log externo com 1.5s e 2.5s | Média exibida 2.00 |
| CLI-03 | JSON | Caminho em diretório novo | Criação, leitura e UTF-8 válidos |

## O que os testes não cobrem

Não há testes de concorrência, ataques com links simbólicos, conjuntos grandes de dados nem integrações externas. Testes de documentação em `tests/test_documentacao.py` não são usados como prova de funcionamento, mas a suíte funcional executa cenários reais.
