candidato = Candidato()
candidato.nome = input("Favor informe o nome do candidato: ")
candidato.legenda = input("Favor informe a legenda do candidato: ")
candidato.numero = int(input("Favor informe o número do candidato: "))
candidato.cargo = input("Favor informe o cargo do candidato: ")
lista.append(candidato)

if (opcao == 2):

    if votos == 100:
        print('O limite de votação foi alcançado')
        continue
    else:
        cont = 0
        for dados in lista:
            cont += 1
            print(str(cont) + " - nome do candidato: " + dados.nome)

        candidato_selecionado = int(input("Escolha qual candidato deseja votar: "))
        candidato_selecionado = candidato_selecionado - 1
        lista[candidato_selecionado].somar_votos(1)
        votos += 1