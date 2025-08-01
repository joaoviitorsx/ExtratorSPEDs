import pandas as pd
from math import ceil
from openpyxl import Workbook
from src.utils.blocos import LAYOUT_REGISTROS

class ExportarService:
    def __init__(self, lote=20000):
        self.chunk_size = lote

    def exportarPlanilha(self, registros, arquivo_saida="sped_exportado.xlsx"):
        print(f"[EXPORTAÇÃO] Iniciando exportação para {arquivo_saida}...")
        
        registros_vazios = []

        with pd.ExcelWriter(arquivo_saida, engine="openpyxl", mode="w") as writer:
            for reg_code, header in LAYOUT_REGISTROS.items():

                if reg_code not in registros or len(registros[reg_code]) == 0:
                    print(f"[EXPORTAÇÃO] ⚠ Nenhum registro '{reg_code}' encontrado. Não será criada aba.")
                    registros_vazios.append(reg_code)
                    continue

                lista_registros = registros[reg_code]
                total_linhas = len(lista_registros)
                total_lotes = ceil(total_linhas / self.chunk_size)

                print(f"[EXPORTAÇÃO] Criando aba '{reg_code}' com {total_linhas:,} linhas em {total_lotes} lote(s)...")

                start = 0
                end = min(self.chunk_size, total_linhas)
                df_inicial = pd.DataFrame([r.campos for r in lista_registros[start:end]])
                df_inicial = self.dataFrame(df_inicial, header)
                df_inicial.to_excel(writer, sheet_name=reg_code[:31], index=False)

                for i in range(1, total_lotes):
                    start = i * self.chunk_size
                    end = min((i + 1) * self.chunk_size, total_linhas)

                    df_lote = pd.DataFrame([r.campos for r in lista_registros[start:end]])
                    df_lote = self.dataFrame(df_lote, header)

                    sheet = writer.sheets[reg_code[:31]]
                    for row in df_lote.to_numpy().tolist():
                        sheet.append(row)

                    print(f"[EXPORTAÇÃO]  -> Lote {i+1}/{total_lotes} exportado ({end-start} linhas).")

                print(f"[EXPORTAÇÃO] Aba '{reg_code}' finalizada ({total_linhas:,} linhas).")

        print(f"[EXPORTAÇÃO] ✅ Arquivo '{arquivo_saida}' gerado com sucesso!")

        return registros_vazios

    def dataFrame(self, df, header):
        if df.shape[1] < len(header):
            for _ in range(len(header) - df.shape[1]):
                df[df.shape[1]] = None
        elif df.shape[1] > len(header):
            df = df.iloc[:, :len(header)]
        df.columns = header
        return df
