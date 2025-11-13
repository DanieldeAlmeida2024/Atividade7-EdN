import json
import os

nome_arquivo = 'dados_pessoa.json'

print("-" * 50)
print("ETAPA 1: Escrevendo dados no arquivo JSON...")
print("-" * 50)

dados_pessoa = {
    "nome": "Ricardo Oliveira",
    "idade": 45,
    "cidade": "Porto Alegre"
}

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados_pessoa, arquivo_json, indent=4)

    print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")
    print(f"Conteúdo escrito: {dados_pessoa}")

except Exception as e:
    print(f"Ocorreu um erro ao escrever no arquivo JSON: {e}")
    exit()

print("-" * 50)
print("ETAPA 2: Lendo dados do arquivo JSON...")
print("-" * 50)

if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado para leitura.")
else:
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_lidos = json.load(arquivo_json)

        print(f"Dados lidos com sucesso do arquivo '{nome_arquivo}'.")
        print("Informações da Pessoa:")
        print(f"  Nome: {dados_lidos['nome']}")
        print(f"  Idade: {dados_lidos['idade']}")
        print(f"  Cidade: {dados_lidos['cidade']}")
        print("-" * 50)

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")