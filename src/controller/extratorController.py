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

            except Exception as e:
                print(f"[ERRO] Falha ao processar {arquivo}: {e}")

            self.processados += 1
            if progresso_callback:
                progresso_callback(self.processados, self.total_arquivos)

        return {
            "status": "sucesso",
            "mensagem": f"{self.total_arquivos} arquivo(s) processado(s) com sucesso!",
            "validos": self.total_arquivos,
            "lista_erros": []
        }

    def exportarPlanilha(self, caminho_saida):
        try:
            self.exportar_service.exportarPlanilha(self.registros_consolidados, caminho_saida)
            return {"status": "sucesso", "mensagem": "Planilha gerada com sucesso!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao exportar a planilha: {e}"}
