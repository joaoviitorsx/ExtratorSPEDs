import pandas as pd
from src.models.spedModel import REGISTROS_SPED
from src.utils.blocos import BLOCOS_SPED

class ExportarService:
    def __init__(self, chunk_size=50000):
        self.chunk_size = chunk_size

    def exportarPlanilha(self, registros, arquivo_saida="sped_exportado.xlsx"):

        print(f"[EXPORTAÇÃO] Iniciando exportação para {arquivo_saida}...")

        with pd.ExcelWriter(arquivo_saida, engine="openpyxl", mode="w") as writer:
            for bloco_nome, codigos in BLOCOS_SPED.items():
                print(f"[EXPORTAÇÃO] Criando aba '{bloco_nome}'...")

                linhas_bloco = []
                for codigo in codigos:
                    if codigo in registros:
                        linhas_bloco.extend([r.campos for r in registros[codigo]])

                if not linhas_bloco:
                    print(f"[EXPORTAÇÃO] ⚠ Nenhum registro encontrado para '{bloco_nome}'. Pulando aba...")
                    continue

                df = pd.DataFrame(linhas_bloco)

                nome_aba = bloco_nome[:31]

                df.to_excel(writer, sheet_name=nome_aba, index=False, header=False)

        print(f"[EXPORTAÇÃO] ✅ Arquivo '{arquivo_saida}' gerado com sucesso!")
