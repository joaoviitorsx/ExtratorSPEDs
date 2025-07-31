import pandas as pd
from models.spedModel import REGISTROS_SPED

class ExportarService:
    def __init__(self, chunk_size=50000):
        self.chunk_size = chunk_size

    def exportar_para_excel(self, registros, arquivo_saida="sped_exportado.xlsx"):
        print(f"[EXPORTAÇÃO] Iniciando exportação para {arquivo_saida}...")

        with pd.ExcelWriter(arquivo_saida, engine="openpyxl", mode="w") as writer:
            for tipo, lista_registros in registros.items():
                print(f"[EXPORTAÇÃO] Criando aba '{tipo}' com {len(lista_registros):,} linhas...")

                linhas = [r.campos for r in lista_registros]

                for i in range(0, len(linhas), self.chunk_size):
                    chunk = linhas[i:i + self.chunk_size]
                    df = pd.DataFrame(chunk)

                    if i == 0:
                        df.to_excel(writer, sheet_name=tipo, index=False, header=False)
                    else:
                        existing_df = pd.read_excel(arquivo_saida, sheet_name=tipo, engine="openpyxl")
                        combined_df = pd.concat([existing_df, df], ignore_index=True)
                        combined_df.to_excel(writer, sheet_name=tipo, index=False, header=False)

                descricao = REGISTROS_SPED.get(tipo, None)
                if descricao:
                    safe_name = descricao[:30]
                    writer.sheets[safe_name] = writer.sheets.pop(tipo)

        print(f"[EXPORTAÇÃO] Arquivo '{arquivo_saida}' gerado com sucesso!")
