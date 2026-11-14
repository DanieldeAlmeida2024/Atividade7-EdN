"""Escrita de dados fictícios em CSV; caminho independente do cwd."""
import argparse
import csv
from pathlib import Path

ARQUIVO_PADRAO = Path(__file__).resolve().parents[1] / "dados_pessoais.csv"
CABECALHOS = ("Nome", "Idade", "Cidade")
AMOSTRA = [
    {"Nome": "Ana Silva", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Bruno Costa", "Idade": 35, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla Mendes", "Idade": 42, "Cidade": "Belo Horizonte"},
]

def escrever_csv(destino: Path, pessoas=AMOSTRA) -> int:
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHOS)
        escritor.writeheader()
        escritor.writerows(pessoas)
    return len(pessoas)

def main():
    parser = argparse.ArgumentParser(description="Escrever exemplo CSV.")
    parser.add_argument("--arquivo", type=Path, default=ARQUIVO_PADRAO)
    args = parser.parse_args()
    try:
        total = escrever_csv(args.arquivo)
    except (OSError, ValueError) as erro:
        parser.error(str(erro))
    print(f"Escritos {total} registros em {args.arquivo}")

if __name__ == "__main__":
    main()
