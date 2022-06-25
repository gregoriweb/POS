'''
Faça um programa que apure o resultado de uma eleição que possua, no máximo, 100 eleitores. 
Suponha que existam 5 candidatos com identificação: Nome, Legenda(Partido) e Número do Candidato, Cargo pleiteado 

O programa deverá possibilitar:

a) Incluir Candidatos

b) Iniciar votação dos candidatos Cadastrados

c) Apurar resultado

     a) Quantidade de votos

      b) Candidatos mais votados

      c) Quantidade de votos nulos e brancos

      d) Vencedor da Eleição
'''

class Candidato:
    nome = None
    legenda = None
    numero = None
    cargoEletivo = None
    numeroVotos = None

    def __init__(self):
        self.nome = ""
        self.legenda = ""
        self.numero = 0
        self.cargoEletivo = ""
        self.numeroVotos = 0

    def somaVotos (self):
        self.numeroVotos += 1

urna = []

maiorNumeroVotos = 0
candidatoMaisVotado = ""
votosNulos = 0
votosTotais = 0
votoValido = 0

while (True):
    print("")
    try: 
        opcao = int(input('''URNA - ELeição 2022
                             1) Incluir Candidato
                             2) Iniciar Votação
                             3) Listar Candidatos
                             4) Exibir Resultado
                             5) Finalizar Eleição
                        '''
    ))
    except ValueError:
       opcao = 0
 

    if(int(opcao) > 5 or int(opcao) < 1):
        print("Opcao Invalida ! ")
        continue
    
    if(int(opcao) == 5):
        break

    if(int(opcao) == 1):
        candidato                   = Candidato()
        candidato.nome              = input("Informe o Nome do candidato: ")
        candidato.legenda           = input("Informe a Legenda do candidato: ")
        candidato.numero            = int( input("Informe o Numero do candidato: ") )
        candidato.cargoEletivo      = input("Informe o Cargo Eletivo do candidato: ")
        urna.append(candidato)

    if(int(opcao) == 2):
        print("Eleição para Prefeito 2022")
        for c in urna:
            print("--------------------------------------------------------\n"
                  "Nome: "+           c.nome               +"\n"+
                  "Legenda: "+        c.legenda            +"\n"+
                  "Numero: "+         str(c.numero)        +"\n"+
                  "Cargo Eletivo: "+  c.cargoEletivo       +"\n"+
                  "--------------------------------------------------------\n"
            )
        
        voto = input("Informe o número do seu candidato: ")
       
        for c in urna:
            if(str(c.numero) == str(voto)):
                c.somaVotos()
                break
            else:
                votosNulos += 1
            
        votosTotais += 1

    if(int(opcao) == 3):
        print("Candidatos Eleição para Prefeito 2022")
        for c in urna:
            print("--------------------------------------------------------\n"
                  "Nome: "+             c.nome             +"\n"+
                  "Legenda: "+          c.legenda          +"\n"+
                  "Numero: "+           str(c.numero)      +"\n"+
                  "Cargo Eletivo: "+    c.cargoEletivo     +"\n"+
                  "--------------------------------------------------------\n"
            )
        
    if(int(opcao) == 4 or votosTotais > 100):

        print("Quantidade de Votos Eleição para Prefeito 2022")
        for c in urna:
            print("--------------------------------------------------------\n"
                  "Nome: "+             c.nome             +" "+
                  "Legenda: "+          c.legenda          +" "+
                  "Numero: "+           str(c.numero)      +" "+
                  "Numero de Votos: "+  str(c.numeroVotos) +"\n"+
                  "--------------------------------------------------------\n"
            )

            if (c.numeroVotos > maiorNumeroVotos):
                maiorNumeroVotos = c.numeroVotos
                candidatoMaisVotado = c.nome
                resultado = candidatoMaisVotado

            elif(c.numeroVotos == maiorNumeroVotos and c.nome != candidatoMaisVotado):
                resultado = "Empate entre " + candidatoMaisVotado +" e "+ c.nome




        if (maiorNumeroVotos == 0):
            print("\nNenhum voto registrado.\n"
            )
        else:
            print("--------------------------------------------------------\n"+
                  "Vencedor da Eleição: " + resultado + "\n" +
                  "Quantidade de Votos Nulos ou Brancos: " + str(votosNulos) + "\n " 
                  "Quantidade de Votos Totais: " + str(votosTotais) + "\n "                 
                 )