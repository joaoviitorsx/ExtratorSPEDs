from src.models.spedModel import RegistroSPED
from collections import defaultdict

class ExtratorService:
    def __init__(self, lote=5000):
        self.lote = lote

    def lerArquivo(self, caminho_arquivo):
        registros = defaultdict(list)
        contador = 0

        with open(caminho_arquivo, "r", encoding="latin-1") as f:
            for linha in f:
                contador += 1
                linha = linha.strip()

                if not linha:
                    continue

                campos = linha.split("|")
                campos = [c for c in campos if c != ""]

                if len(campos) < 2:
                    continue

                if len(campos) < 1:
                    continue

                tipo = campos[0]
                registro = RegistroSPED(tipo=tipo, campos=campos)
                registros[tipo].append(registro)

        return registros
