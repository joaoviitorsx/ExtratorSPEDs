from dataclasses import dataclass

@dataclass
class RegistroSPED:
    tipo: str
    campos: list

REGISTROS_SPED = {
    # Abertura e Identificação
    "0000": "Abertura do Arquivo Digital e Identificação da Pessoa Jurídica",

    # Tabelas
    "0140": "Tabela de Estabelecimentos, Obras ou Unidades Autônomas",
    "0150": "Tabela de Participantes",
    "0190": "Identificação das Unidades de Medida",
    "0200": "Tabela de Identificação do Item (Produtos e Serviços)",
    "0400": "Tabela de Natureza da Operação/Prestação",

    # Bloco A
    "A100": "Documento - Nota Fiscal de Serviço (NFS-e)",
    "A111": "Processo Referenciado",
    "A170": "Itens do Documento",

    # Bloco C
    "C100": "Documento - Nota Fiscal (Modelos 01, 1A, NF-e)",
    "C111": "Processo Referenciado",
    "C120": "Operações de Importação",
    "C170": "Itens do Documento",
    "C175": "Operações com Produtos Sujeitos ao Regime de Substituição Tributária",
    "C180": "Resumo de Documentos Emitidos por ECF (Emissor de Cupom Fiscal)",
    "C181": "Detalhamento dos Documentos Emitidos por ECF",
    "C185": "Resumo de Documentos Emitidos por Equipamento SAT-CF-e",
    "C186": "Detalhamento dos Documentos Emitidos por SAT-CF-e",
    "C190": "Resumo por CFOP e CST",

    # Bloco D
    "D100": "Documento - Nota Fiscal de Serviço de Transporte",
    "D105": "Detalhamento da Contribuição por Item (PIS/Pasep e Cofins)",
    "D200": "Documento - Nota Fiscal de Serviço de Comunicação",
    "D205": "Detalhamento da Contribuição por Item (Comunicação)",
    "D500": "Documento - Nota Fiscal de Serviço de Comunicação - Entrada",
    "D505": "Detalhamento da Contribuição por Item (Entradas)",

    #Bloco F
    "F100": "Demais Documentos e Operações Geradoras de Contribuição",
    "F120": "Operações com Direito a Crédito - Documentos de Importação",
    "F130": "Receitas Financeiras",
    "F150": "Receitas de Exportação",
    "F200": "Operações com Direito a Crédito Presumido - Combustíveis",
    "F205": "Detalhamento do Crédito Presumido - Combustíveis",
    "F210": "Detalhamento do Crédito Presumido - Demais Situações",
    "F600": "Consolidação das Contribuições sobre Demais Receitas",
    "F700": "Consolidação dos Créditos Presumidos",
    "F800": "Demais Documentos e Operações Geradoras de Contribuição - Específicos",

    #Bloco M
    "M100": "Créditos de PIS/Pasep - Apuração do Período",
    "M105": "Detalhamento dos Créditos de PIS/Pasep",
    "M110": "Consolidação dos Créditos de PIS/Pasep",
    "M115": "Detalhamento da Base de Cálculo e Contribuição de PIS/Pasep",
    "M200": "Consolidação da Contribuição para o PIS/Pasep",
    "M205": "Detalhamento dos Débitos de PIS/Pasep",
    "M210": "Débitos de Cofins - Apuração do Período",
    "M211": "Detalhamento da Base de Cálculo e Contribuição de Cofins",
    "M215": "Ajustes da Apuração de Cofins",
    "M220": "Créditos de Cofins - Apuração do Período",
    "M225": "Detalhamento dos Créditos de Cofins",
    "M230": "Consolidação dos Créditos de Cofins",
    "M235": "Detalhamento da Base de Cálculo e Contribuição de Cofins",
    "M300": "Consolidação da Contribuição para Cofins",
    "M305": "Detalhamento dos Débitos de Cofins",
    "M350": "Base de Cálculo da CPRB - PIS/Pasep e Cofins",
    "M400": "Créditos Presumidos - PIS/Pasep e Cofins",
    "M410": "Detalhamento dos Créditos Presumidos",
    "M500": "Créditos de Retenção - PIS/Pasep e Cofins",
    "M505": "Detalhamento dos Créditos de Retenção",
    "M600": "Consolidação da Apuração do PIS/Pasep",
    "M605": "Ajustes da Apuração do PIS/Pasep",
    "M610": "Consolidação da Apuração do Cofins",
    "M615": "Ajustes da Apuração do Cofins",

    #Bloco P
    "P100": "Receitas auferidas sujeitas à CPRB",
    "P200": "Apuração da CPRB",
    "P210": "Detalhamento da Base de Cálculo da CPRB"
}

def getRegistro(tipo: str) -> str:
    return REGISTROS_SPED.get(tipo, "Registro não documentado")
