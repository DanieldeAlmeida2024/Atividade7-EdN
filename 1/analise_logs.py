import re
import statistics

log_content = """
[INFO] Inicializando o treinamento do Modelo X...
[ETAPA 1] Pré-processamento concluído em 5.2s.
[TREINO] Época 1/10. Loss: 0.85. Execution Time: 12.3s
[TREINO] Época 2/10. Loss: 0.71. Execution Time: 13.5s
[TREINO] Época 3/10. Loss: 0.62. Execution Time: 14.1s
[TREINO] Época 4/10. Loss: 0.55. Execution Time: 12.9s
[TREINO] Época 5/10. Loss: 0.48. Execution Time: 15.0s
[TREINO] Época 6/10. Loss: 0.41. Execution Time: 13.2s
[TREINO] Época 7/10. Loss: 0.35. Execution Time: 14.8s
[TREINO] Época 8/10. Loss: 0.29. Execution Time: 12.7s
[TREINO] Época 9/10. Loss: 0.24. Execution Time: 15.5s
[TREINO] Época 10/10. Loss: 0.19. Execution Time: 14.0s
[INFO] Treinamento concluído.
"""

regex = r"Execution Time: (\d+\.?\d*)s"

tempos_str = re.findall(regex, log_content)

try:
    tempos_float = [float(t) for t in tempos_str]

    if tempos_float:
        media_tempo = statistics.mean(tempos_float)
        desvio_padrao = statistics.stdev(tempos_float)

        print("-" * 50)
        print("Análise dos Tempos de Execução do Modelo de ML")
        print("-" * 50)
        print(f"Tempos de execução encontrados: {tempos_float} segundos")
        print(f"Média do Tempo de Execução: {media_tempo:.2f} segundos")
        print(f"Desvio Padrão do Tempo de Execução: {desvio_padrao:.2f} segundos")
        print("\nOs tempos de execução foram extraídos e as estatísticas calculadas com sucesso.")
    else:
        print("Nenhum tempo de execução encontrado no log simulado.")

except ValueError as e:
    print(f"Erro ao converter dados de tempo para float: {e}")
    print("Verifique o formato dos dados no log simulado.")