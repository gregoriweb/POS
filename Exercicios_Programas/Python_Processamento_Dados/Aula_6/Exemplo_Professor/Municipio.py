class Municipio():

    

    def __init__(self):

        self.nome_municipio = ""

        self.expectativa = 0.0

        self.mortalidade = 0.0

        self.cod_municipio = 0

        self.ano = 0



    def as_dict_mortalidade(self):

        return {'Municipio': self.nome_municipio,

                'Mortalidade': self.mortalidade,

               }



    def as_dict_expectativa(self):

        return {'Municipio': self.nome_municipio,

                'Expectativa': self.expectativa,

               }