"""Escrita e leitura de JSON de exemplo, com validação estrutural."""
import argparse
import json
from pathlib import Path

ARQUIVO_PADRAO = Path(__file__).resolve().parents[1] / "dados_pessoa.json"
AMOSTRA = {"nome": "Ricardo Oliveira", "idade": 45, "cidade": "Porto Alegre"}

def escrever_json(destino: Path, pessoa=AMOSTRA) -> None:
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=2, allow_nan=False)

def ler_json(origem: Path) -> dict:
    with Path(origem).open("r", encoding="utf-8") as arquivo:
        pessoa = json.load(arquivo)
    if (not isinstance(pessoa, dict) or
        not isinstance(pessoa.get("nome"), str) or not pessoa["nome"].strip() or
        type(pessoa.get("idade")) is not int or not 0 <= pessoa["idade"] <= 130 or
        not isinstance(pessoa.get("cidade"), str) or not pessoa["cidade"].strip()):
        raise ValueError("JSON deve conter nome e cidade como texto e idade de 0 a 130.")
    return pessoa

def main():
    parser = argparse.ArgumentParser(description="Escrever e ler JSON didático.")
    parser.add_argument("--arquivo", type=Path, default=ARQUIVO_PADRAO)
    args = parser.parse_args()
    try:
        escrever_json(args.arquivo)
        pessoa = ler_json(args.arquivo)
    except (OSError, ValueError, TypeError) as erro:
        parser.error(str(erro))
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade: {pessoa['cidade']}")

if __name__ == "__main__":
    main()
