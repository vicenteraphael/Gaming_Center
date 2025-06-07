def mudar (mesa, nPecas):
    while True:
        try:
            src, dest = input("Faça sua mudança:\n\n<Nº ARGOLA FONTE> <Nº ARGOLA DESTINO>\n\n").split()
            src, dest = int(src)-1, int(dest)-1
            if 0 <= src != dest <= 2:
                break
            else:
                raise Exception
        except:
            print ("MOVIMENTO INVÁLIDO")
            return False
    try:
        u = mesa[src][-1]
    except:
        print ("MOVIMENTO INVÁLIDO")
        return False
    if (len(mesa[dest]) == 0 or (u < mesa[dest][-1] and len(mesa[dest]) != nPecas)):
        mesa[dest].append(u)
        mesa[src].pop()
    else:
        print ("MOVIMENTO INVÁLIDO")
    if len(mesa[dest]) == nPecas:
        return True
    return False


def jogo():
    n = int(input("Número de peças: "))
    print()
    mesa = [[i for i in range(n, 0, -1)], [], []]
    while True:
        for i in range(n-1, -1, -1):
            for j in range (0, 3):
                try:
                    print (mesa[j][i], "   ", end='')
                except:
                    print ("     ", end='')
            print()
        print("|____|____|")
        if mudar(mesa, n):
            return True
        
        
while True:
    match input("Escolha:\n\n1) Jogar\n2) Sair\n\n"):
        case "1":
            if jogo():
                print ("VOCÊ GANHOU!")
        case "2":
            break
        case _:
            print ("Erro")