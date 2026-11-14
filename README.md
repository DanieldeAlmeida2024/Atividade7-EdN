# Atividade 07 — Logs de treinamento, CSV e JSON

Quatro exercícios de Python voltados a arquivos e análise de dados. Os exemplos usam dados fictícios e apenas a biblioteca padrão.

## Executar

Com **Python 3.10+**, a partir da raiz do projeto:

```bash
python 1/analise_logs.py
python 2/escrever_csv.py
python 3/ler_csv.py
python 4/manipular_json.py
```

O segundo comando cria ou substitui `dados_pessoais.csv`; o quarto cria ou substitui `dados_pessoa.json`. Os caminhos padrão são relativos à **raiz do repositório**, não à pasta de onde o comando foi executado.

Para trabalhar em uma pasta de testes, sem sobrescrever os exemplos:

```bash
python 1/analise_logs.py --arquivo ./treinamento.log
python 2/escrever_csv.py --arquivo ./tmp/pessoas.csv
python 3/ler_csv.py --arquivo ./tmp/pessoas.csv
python 4/manipular_json.py --arquivo ./tmp/pessoa.json
```

## O que cada exercício demonstra

| Script | Responsabilidade | Tratamento |
| --- | --- | --- |
| `1/analise_logs.py` | Extrai tempos `Execution Time: Xs`, calcula média e desvio-padrão **amostral** | Um único tempo retorna desvio 0; ausência de tempos é erro explícito |
| `2/escrever_csv.py` | Escreve nomes fictícios, idades e cidades em CSV UTF-8 | Cria diretório destino e preserva acentos |
| `3/ler_csv.py` | Lê CSV com `Nome,Idade,Cidade` | Rejeita cabeçalhos inesperados, idades inválidas e linhas incompletas |
| `4/manipular_json.py` | Grava e relê JSON de uma pessoa fictícia | Valida estrutura, tipos, idade e Unicode |

## Testes reais

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Os testes incluem roundtrip CSV/JSON, arquivos malformados, estatísticas com uma ou várias épocas e execução dos scripts a partir de outro diretório. O GitHub Actions roda essa suíte em PRs e na `main`.

**Limites:** exercícios de arquivo local, sem autenticação, dados reais, armazenamento criptografado ou serviço HTTP. O desvio é amostral (`statistics.stdev`), não populacional.

## Documentação

- [Arquitetura e responsabilidades](docs/ARQUITETURA.md)
- [Modelo UML](docs/UML.puml)
- [Plano de testes e critérios](docs/PLANO_TESTES.md)
- [Enunciados e requisitos](docs/REQUISITOS.md)
