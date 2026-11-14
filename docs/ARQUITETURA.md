# Arquitetura — Atividade 07

Versão 1.1.0 — 14/11/2026

## Componentes

- **Análise de logs** (`1/analise_logs.py`): `analisar_tempos(texto)` extrai tempos positivos com regex, converte para `float`, calcula média e desvio amostral. `main()` recebe `--arquivo` ou usa a amostra.
- **Escrita CSV** (`2/escrever_csv.py`): `escrever_csv(caminho, pessoas)` cria o diretório de saída e usa `csv.DictWriter`; amostra de três pessoas fictícias.
- **Leitura CSV** (`3/ler_csv.py`): `ler_csv(caminho)` abre UTF-8 com ou sem BOM, valida cabeçalhos exatos e converte `Idade` para inteiro.
- **JSON** (`4/manipular_json.py`): `escrever_json` grava objeto com `ensure_ascii=False`; `ler_json` carrega, valida tipos e intervalo etário.

## Fluxo e decisões

Os quatro scripts são executáveis independentes. As funções são puras no caso da análise e de caminho explícito nos casos de I/O, permitindo testes isolados e sem acesso a serviços externos.

A saída padrão dos exercícios CSV/JSON é resolvida em relação a `Path(__file__).resolve().parents[1]`. Isso evita erros quando o estudante executa os scripts em outro diretório.

**Limites:** sobrescrita intencional do arquivo destino, amostras fictícias, nenhum controle de concorrência e nenhum contrato de serviço HTTP. Para persistência de dados reais seriam necessários consentimento, controles de acesso e proteção dos arquivos.

## Evolução

- v1.0: scripts de exemplo baseados em caminhos relativos ao processo, sem testes funcionais.
- v1.1: funções reutilizáveis, caminho estável, validação de arquivos, CLIs parametrizáveis e testes comportamentais.
