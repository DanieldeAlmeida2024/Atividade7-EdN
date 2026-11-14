"""Leitura e validação das colunas do exemplo CSV."""
import argparse
import csv
from pathlib import Path

ARQUIVO_PADRAO = Path(__file__).resolve().parents[1] / "dados_pessoais.csv"
CABECALHOS = ("Nome", "Idade", "Cidade")

def ler_csv(origem: Path) -> list[dict]:
    origem = Path(origem)
    with origem.open("r", newline="", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)
        if leitor.fieldnames != list(CABECALHOS):
            raise ValueError("CSV deve ter as colunas: Nome,Idade,Cidade")
        resultado = []
        for numero, linha in enumerate(leitor, start=2):
            try:
                idade = int(linha["Idade"])
                if not 0 <= idade <= 130:
                    raise ValueError()
                nome, cidade = linha["Nome"].strip(), linha["Cidade"].strip()
                if not nome or not cidade:
                    raise ValueError()
            except (ValueError, TypeError, KeyError, AttributeError) as erro:
                raise ValueError(f"Linha {numero}: pessoa inválida.") from erro
            resultado.append({"Nome": nome, "Idade": idade, "Cidade": cidade})
        return resultado

def main():
    parser = argparse.ArgumentParser(description="Ler exemplo CSV.")
    parser.add_argument("--arquivo", type=Path, default=ARQUIVO_PADRAO)
    args = parser.parse_args()
    try:
        pessoas = ler_csv(args.arquivo)
    except (OSError, ValueError) as erro:
        parser.error(str(erro))
    for indice, pessoa in enumerate(pessoas, start=1):
        print(f"{indice}. {pessoa['Nome']} — {pessoa['Idade']} anos — {pessoa['Cidade']}")
    print(f"Registros lidos: {len(pessoas)}")

if __name__ == "__main__":
    main()
