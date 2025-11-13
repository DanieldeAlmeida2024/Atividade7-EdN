import csv
import os

nome_arquivo = '../dados_pessoais.csv'

dados = [
    {'Nome': 'Ana Silva', 'Idade': 28, 'Cidade': 'São Paulo'},
    {'Nome': 'Bruno Costa', 'Idade': 35, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Carla Mendes', 'Idade': 42, 'Cidade': 'Belo Horizonte'}
]

cabecalhos = ['Nome', 'Idade', 'Cidade']

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)

        escritor_csv.writeheader()

        escritor_csv.writerows(dados)

    if os.path.exists(nome_arquivo):
        print("-" * 50)
        print(f"Sucesso! O arquivo '{nome_arquivo}' foi criado.")
        print(f"Dados pessoais escritos com os cabeçalhos: {cabecalhos}")
        print("-" * 50)
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado após a tentativa de escrita.")

except Exception as e:
    print(f"Ocorreu um erro ao escrever no arquivo CSV: {e}")