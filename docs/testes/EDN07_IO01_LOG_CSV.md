# EDN07-IO-01 — Estatísticas de logs e escrita CSV sem perda

14/11/2026 · Exercícios 1 e 2 da Atividade 7.

## Falhas
O regex extraía um tempo negativo como se fosse positivo: `Execution Time: -1.0s` podia virar `1.0`. Um número decimal muito grande era convertido para infinito e contaminava as estatísticas. A escrita de CSV truncava imediatamente um destino existente e podia falhar após gravar só parte dos registros.

## Contratos novos
- Valores negativos ou não finitos de tempos geram ValueError em vez de métricas falsas.
- Arquivos CSV são gerados em arquivo temporário no mesmo diretório, substituindo o destino somente após escrita completa; falhas preservam bytes existentes.
- Testes verificam números adversariais e preservação do arquivo em erro de coluna inesperada.

## Limite
Não é parser de logs de produção, sistema de backup ou mecanismo de sincronização multiusuário. Escrita atômica depende de filesystem que suporte replace no mesmo volume.
