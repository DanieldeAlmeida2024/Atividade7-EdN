import csv
import os

nome_arquivo = '../dados_pessoais.csv'

print("-" * 50)
print(f"Lendo dados do arquivo CSV: '{nome_arquivo}'")
print("-" * 50)

if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Execute o script 'escrever_csv.py' primeiro para criar o arquivo.")
else:
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            cabecalhos = leitor_csv.fieldnames
            print(f"Cabeçalhos: {cabecalhos}")
            print("-" * 50)

            for i, linha in enumerate(leitor_csv):
                print(f"Registro {i+1}:")
                print(f"  Nome: {linha['Nome']}")
                print(f"  Idade: {linha['Idade']}")
                print(f"  Cidade: {linha['Cidade']}")
                print("-" * 50)

            print("Leitura do arquivo CSV concluída com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")