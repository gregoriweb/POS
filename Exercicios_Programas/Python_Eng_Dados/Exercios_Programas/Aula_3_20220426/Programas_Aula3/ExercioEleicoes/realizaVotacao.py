'''
Atividade 2:
aça um programa que apure o resultado de uma 
eleição que possua, no máximo, 100 eleitores. 
Suponha que existam 5 candidatos com 
identificação: Nome, Legenda(Partido) e 
Número do Candidato, Cargo pleiteado 
'''



from ExercioEleicoes.OO.Candidato import Candidato


urna = []
opcao = 0

while(True):
    print("")
    opcao = int(input( '''
                        Escolha a opção para efetuar a eleição:
                        1)  Adicionar um candidato
                        2)  Listar candidatos cadastrados
                        3)  Iniciar Eleição
                        4)  Finalizar Eleição
                        '''
                        ))

    if(opcao > 3 or opcao < 1):
        print("Opcao Invalida ! ")
        continue
    
    if(opcao == 4):
        break
    
    if (opcao == 1):
        candidato = Candidato()
        candidato.nome = input("Favor informe o nome do candidato: ")
        candidato.cargoEletivo = input("Favor informe o cargo do Candidato: ")
        candidato.numero = int(input("Favor informe o número do Candidato: "))
        candidato.legenda = int(input("Favor informe a legenda do Candidato: "))
        urna.append(candidato)
    
    if(opcao == 2):
        print("Eleição Prefeito")
        for candidato in urna:
            print (
                "Partido:"  + candidato.nome + "\n"
                "Nome:"     + candidato.cargoEletivo + "\n"
                "Numero:"   + candidato.numero + "\n"
                "cargo:"    + candidato.cargoEletivo + "\n"
                "legenda:"  + candidato.legenda + "\n"
                )
        
        candSelecionado = int(input("Escolha o numero do candidato: "))

        for candidato in urna:
            if (candidato.numero == candSelecionado):
                candidato.