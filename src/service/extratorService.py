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

                if len(campos) < 2:
                    continue

                tipo = campos[1]

                registro = RegistroSPED(tipo=tipo, campos=campos)
                registros[tipo].append(registro)

                if contador % self.lote == 0:
                    print(f"[INFO] {contador:,} linhas processadas até agora...")

        print(f"[FINALIZADO] {contador:,} linhas processadas.")
        return registros
