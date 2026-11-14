"""Análise de tempo de execução de treinamento em logs."""
import argparse
import re
import statistics
from pathlib import Path

AMOSTRA_LOG = "\n[INFO] Inicializando o treinamento do Modelo X...\n[ETAPA 1] Pré-processamento concluído em 5.2s.\n[TREINO] Época 1/10. Loss: 0.85. Execution Time: 12.3s\n[TREINO] Época 2/10. Loss: 0.71. Execution Time: 13.5s\n[TREINO] Época 3/10. Loss: 0.62. Execution Time: 14.1s\n[TREINO] Época 4/10. Loss: 0.55. Execution Time: 12.9s\n[TREINO] Época 5/10. Loss: 0.48. Execution Time: 15.0s\n[TREINO] Época 6/10. Loss: 0.41. Execution Time: 13.2s\n[TREINO] Época 7/10. Loss: 0.35. Execution Time: 14.8s\n[TREINO] Época 8/10. Loss: 0.29. Execution Time: 12.7s\n[TREINO] Época 9/10. Loss: 0.24. Execution Time: 15.5s\n[TREINO] Época 10/10. Loss: 0.19. Execution Time: 14.0s\n[INFO] Treinamento concluído.\n"
PADRAO_TEMPO = re.compile(r"Execution Time:\s*(\d+(?:\.\d+)?)s\b")

def analisar_tempos(conteudo: str) -> dict:
    if not isinstance(conteudo, str):
        raise TypeError("O log deve ser texto.")
    tempos = [float(tempo) for tempo in PADRAO_TEMPO.findall(conteudo)]
    if not tempos:
        raise ValueError("Nenhum tempo de execução encontrado no log.")
    return {
        "tempos": tempos,
        "media": statistics.mean(tempos),
        "desvio_padrao_amostral": statistics.stdev(tempos) if len(tempos) > 1 else 0.0,
    }

def main():
    parser = argparse.ArgumentParser(description="Estatísticas de tempo de execução (s).")
    parser.add_argument("--arquivo", type=Path, help="Log UTF-8; sem arquivo, usa a amostra didática.")
    args = parser.parse_args()
    try:
        conteudo = args.arquivo.read_text(encoding="utf-8") if args.arquivo else AMOSTRA_LOG
        resultado = analisar_tempos(conteudo)
    except (OSError, ValueError, TypeError) as erro:
        parser.error(str(erro))
    print(f"Épocas encontradas: {len(resultado['tempos'])}")
    print(f"Média: {resultado['media']:.2f} segundos")
    print(f"Desvio padrão amostral: {resultado['desvio_padrao_amostral']:.2f} segundos")

if __name__ == "__main__":
    main()
