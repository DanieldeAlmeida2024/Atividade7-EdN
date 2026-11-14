"""Regressões dos exercícios de log, CSV e JSON sem arquivo global."""
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

RAIZ = pathlib.Path(__file__).resolve().parents[1]

def modulo(nome, caminho):
    especificacao = importlib.util.spec_from_file_location(nome, RAIZ / caminho)
    objeto = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(objeto)
    return objeto

logs = modulo("analise_logs", "1/analise_logs.py")
csv_writer = modulo("escrever_csv", "2/escrever_csv.py")
csv_reader = modulo("ler_csv", "3/ler_csv.py")
json_io = modulo("manipular_json", "4/manipular_json.py")


class TestesAtividade07(unittest.TestCase):
    def test_log_amostra_tem_dez_epocas(self):
        resultado = logs.analisar_tempos(logs.AMOSTRA_LOG)
        self.assertEqual(10, len(resultado["tempos"]))
        self.assertAlmostEqual(12.3, resultado["tempos"][0])
        self.assertGreater(resultado["desvio_padrao_amostral"], 0)

    def test_log_uma_epoca_nao_divide_por_zero(self):
        resultado = logs.analisar_tempos("Execution Time: 12.3s")
        self.assertEqual(12.3, resultado["media"])
        self.assertEqual(0, resultado["desvio_padrao_amostral"])

    def test_log_sem_tempo_falha_explicita(self):
        with self.assertRaisesRegex(ValueError, "Nenhum tempo"):
            logs.analisar_tempos("modelo iniciou mas não executou")

    def test_csv_roundtrip_preserva_acentos(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "sub" / "pessoas.csv"
            total = csv_writer.escrever_csv(arquivo)
            resultado = csv_reader.ler_csv(arquivo)
            self.assertEqual(3, total)
            self.assertEqual(3, len(resultado))
            self.assertEqual("São Paulo", resultado[0]["Cidade"])
            self.assertIsInstance(resultado[0]["Idade"], int)

    def test_csv_sem_cabecalho_esperado(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "pessoas.csv"
            arquivo.write_text("Nome,Cidade\nAna,SP\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "colunas"):
                csv_reader.ler_csv(arquivo)

    def test_csv_idade_invalida_e_registro_incompleto(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "pessoas.csv"
            for conteudo in ("Nome,Idade,Cidade\nAna,-10,SP\n",
                             "Nome,Idade,Cidade\nAna,abc,SP\n",
                             "Nome,Idade,Cidade\nAna,30\n"):
                with self.subTest(conteudo=conteudo):
                    arquivo.write_text(conteudo, encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "Linha 2"):
                        csv_reader.ler_csv(arquivo)

    def test_json_roundtrip_preserva_unicode(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "resultado" / "pessoa.json"
            pessoa = {"nome": "João", "idade": 25, "cidade": "Goiânia"}
            json_io.escrever_json(arquivo, pessoa)
            self.assertIn("Goiânia", arquivo.read_text(encoding="utf-8"))
            self.assertEqual(pessoa, json_io.ler_json(arquivo))

    def test_json_malformado_e_estrutura_invalida(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "pessoa.json"
            for valor in ("{}", '{"nome":"Ana","idade":true,"cidade":"SP"}', 'invalido'):
                with self.subTest(valor=valor):
                    arquivo.write_text(valor, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        json_io.ler_json(arquivo)

    def test_cli_csv_funciona_independente_do_diretorio_atual(self):
        with tempfile.TemporaryDirectory() as pasta:
            destino = pathlib.Path(pasta) / "dados_pessoais.csv"
            escrever = subprocess.run(
                [sys.executable, str(RAIZ / "2/escrever_csv.py"), "--arquivo", str(destino)],
                cwd=pasta, capture_output=True, text=True, timeout=10
            )
            ler = subprocess.run(
                [sys.executable, str(RAIZ / "3/ler_csv.py"), "--arquivo", str(destino)],
                cwd=pasta, capture_output=True, text=True, timeout=10
            )
            self.assertEqual(0, escrever.returncode, escrever.stderr)
            self.assertEqual(0, ler.returncode, ler.stderr)
            self.assertIn("Registros lidos: 3", ler.stdout)
            self.assertIn("São Paulo", ler.stdout)

    def test_cli_log_arquivo_externo_e_saida(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "treino.log"
            arquivo.write_text("Execution Time: 1.5s\nExecution Time: 2.5s\n", encoding="utf-8")
            p = subprocess.run(
                [sys.executable, str(RAIZ / "1/analise_logs.py"), "--arquivo", str(arquivo)],
                cwd=pasta, capture_output=True, text=True, timeout=10
            )
            self.assertEqual(0, p.returncode, p.stderr)
            self.assertIn("Média: 2.00", p.stdout)

    def test_cli_json_diretorio_alternativo(self):
        with tempfile.TemporaryDirectory() as pasta:
            destino = pathlib.Path(pasta) / "resultado" / "pessoa.json"
            p = subprocess.run(
                [sys.executable, str(RAIZ / "4/manipular_json.py"), "--arquivo", str(destino)],
                cwd=pasta, capture_output=True, text=True, timeout=10
            )
            self.assertEqual(0, p.returncode, p.stderr)
            self.assertEqual("Ricardo Oliveira", json.loads(destino.read_text(encoding="utf8"))["nome"])


if __name__ == "__main__":
    unittest.main()
