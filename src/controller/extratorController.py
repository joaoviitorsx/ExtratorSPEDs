import os
from src.service.extratorService import ExtratorService
from src.service.exportarService import ExportarService

class ExtratorController:
    def __init__(self):
        self.extrator_service = ExtratorService()
        self.exportar_service = ExportarService()
        self.registros_consolidados = {}
        self.total_arquivos = 0
        self.processados = 0

    def processarPasta(self, pasta_entrada, progresso_callback=None):
        if not os.path.isdir(pasta_entrada):
            return {"status": "erro", "mensagem": f"Pasta '{pasta_entrada}' não encontrada."}

        arquivos_sped = [
            f for f in os.listdir(pasta_entrada)
            if f.lower().endswith(".txt") and os.path.isfile(os.path.join(pasta_entrada, f))
        ]

        self.total_arquivos = len(arquivos_sped)
        self.processados = 0
        self.registros_consolidados.clear()
        lista_erros = []

        if self.total_arquivos == 0:
            return {"status": "erro", "mensagem": "Nenhum arquivo SPED (.txt) encontrado na pasta."}

        for arquivo in arquivos_sped:
            caminho_arquivo = os.path.join(pasta_entrada, arquivo)
            try:
                registros = self.extrator_service.lerArquivo(caminho_arquivo)

                for tipo, lista in registros.items():
                    if tipo not in self.registros_consolidados:
                        self.registros_consolidados[tipo] = []
                    self.registros_consolidados[tipo].extend(lista)

                print(f"[PROCESSAMENTO] ✅ {arquivo} processado ({len(registros)} tipos de registros).")

            except Exception as e:
                erro_msg = f"Falha ao processar {arquivo}: {e}"
                print(f"[ERRO] ❌ {erro_msg}")
                lista_erros.append(erro_msg)

            self.processados += 1
            if progresso_callback:
                progresso_callback(self.processados, self.total_arquivos)

        total_registros = sum(len(lst) for lst in self.registros_consolidados.values())

        return {
            "status": "sucesso",
            "mensagem": f"{self.total_arquivos} arquivo(s) processado(s) com sucesso! Total de {total_registros:,} registros consolidados.",
            "validos": self.total_arquivos - len(lista_erros),
            "lista_erros": lista_erros
        }

    def exportarPlanilha(self, caminho_saida):
        try:
            pasta_destino = os.path.dirname(caminho_saida)
            if pasta_destino and not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            registros_vazios = self.exportar_service.exportarPlanilha(self.registros_consolidados, caminho_saida)

            self.registros_consolidados.clear()

            return {
                "status": "sucesso",
                "mensagem": f"Planilha gerada com sucesso em: {caminho_saida}",
                "registros_vazios": registros_vazios
            }
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao exportar a planilha: {e}"}

