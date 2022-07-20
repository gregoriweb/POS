from faker import Faker
from random import randrange
import pandas as pd

class Aluno:
    
    def __init__(self):
        self.nome = ""
        self.notas = 0.0
        self.faltas = 0
        self.descricao_prova = ""
        
    def as_dict(self):
        return {'Nome': self.nome,
                'Faltas': self.faltas,
                'Notas': self.notas,
                'Descrição':self.descricao_prova}



def popular_aluno(numero_alunos):
    lista_alunos = []
    fake = Faker()

    for x in range(numero_alunos):
        aluno = Aluno()
        aluno.nome = fake.name()
        aluno.faltas = randrange(1, 30, 1)
        aluno.descricao_prova = fake.text()
        aluno.notas = randrange(40, 100, 5)
        lista_alunos.append(aluno)
     
    return lista_alunos   


lista = popular_aluno(50)
df = pd.DataFrame([x.as_dict() for x in lista])
file_name = 'Exercicio_Aula2.xlsx'
df.to_excel(file_name)