import os

class DestinoDados:
    def __init__(self,dataset=[],destiny_folder="./",destiny_file="saida.txt") -> None:
        self.endereco_arquivo = os.path.join(os.path.dirname(__file__) , destiny_folder, destiny_file)
        self.dataset = dataset

    def populaArquivo(self, dataset=[], arquivo="saida.txt", pasta_arquivo="./", spliter=";", charset="utf-8"):

        #remove arquivo caso já exista
        if os.path.exists(self.endereco_arquivo):
            os.remove(self.endereco_arquivo)

        if len(dataset) == 0:
            dataset = self.dataset
        
        for i in dataset:
            i = spliter.join(i)
            arquivo = open(self.endereco_arquivo, "a", encoding=charset)
            arquivo.writelines(i)
