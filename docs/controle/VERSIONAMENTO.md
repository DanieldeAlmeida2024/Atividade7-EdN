> **Referência histórica de 11/11/2026.** A execução atual e as alterações posteriores estão no README e em `docs/PLANO_TESTES.md` da main. Não tratar estados históricos como evidências de homologação.

# Versões documentais — Atividade7-EdN

**v1.0.0**, 11/11/2026 · base do código `b6d049208972ee62b6f7acc5c39b1e666776d392`.

| Documento | ID | Versão |
|---|---|---|
| [Projeto](../projeto/ESPECIFICACAO.md) | Atividade7-EdN-PROJ | 1.0.0 |
| [UML](../uml/README.md) | Atividade7-EdN-UML | 1.0.0 |
| [Testes](../testes/PLANO_DE_TESTES.md) | Atividade7-EdN-TST | 1.0.0 |

MAJOR para quebra de contrato, MINOR para novas funcionalidades/casos, PATCH para edição. Para cada revisão, anexar o SHA, ambiente e evidências de testes por cenário.

## Reconciliação documental de 14/11/2026

Especificações e UML históricas migradas para a `main` atual com aviso de escopo, sem substituir testes, arquitetura ou código posteriores. O CI vigente continua sendo a fonte de evidência funcional.

## Escrita JSON · 24/11/2026

- [Arquitetura 1.1.1](../ARQUITETURA.md) descreve a substituição do destino após uma gravação completa.
- [Plano de testes 1.2.0](../PLANO_TESTES.md) acrescenta JSON-03 e JSON-04 para preservação do destino e limpeza de temporários.
- Código validado em `952bd57bd898096568b3e22e0c861de6728a6770`. Python 3.11.9 executou `python -m unittest discover -s tests -p 'test_*.py' -v` com 17 testes aprovados e `python -m compileall -q 1 2 3 4 tests` sem erros.
