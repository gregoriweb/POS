import os

class FonteDados:
    def __init__(self) -> None:
        self.arquivo = ""
        self.dataset = []

    def vetorArquivo(self, arquivo="", pasta_arquivo="../arquivos", spliter=";", charset="utf-8"):
        endereco_arquivo = os.path.join(os.path.dirname(__file__) , pasta_arquivo, arquivo)
        linhas = open(endereco_arquivo, "r", encoding=charset)
     
        for linha in linhas.readlines():
            self.dataset.append(linha.split(spliter))
        
        linhas.close