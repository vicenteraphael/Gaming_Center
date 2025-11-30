from random import randint

def inicializar_tabuleiro (dimensoes):
    tabuleiro = [["-" for _ in range (dimensoes)] for _ in range (dimensoes)]

    cnt = 0
    while cnt < dimensoes:
        x = randint(0, dimensoes-1)
        y = randint(0, dimensoes-1)
        if tabuleiro[y][x] != 1:
            tabuleiro[y][x] = 1
            cnt += 1

    return tabuleiro

def mostrar_tabuleiro(tabuleiro, id, dimensoes, letras):
    if id == 0: #usuário
        print ("SEU TABULEIRO")
        for x in range (dimensoes):
            print (letras[x], "", end='')
            for y in range (dimensoes):
                print (tabuleiro[x][y], "", end='')
            print()
    else: #máquina
        print ("TABULEIRO DA MÁQUINA")
        for x in range (dimensoes):
            print (letras[x], "", end='')
            for y in range (dimensoes):
                if (tabuleiro[x][y] == 1):
                    print (f"- ", end='')
                else:
                    print (tabuleiro[x][y], "", end='')
            print ()
    print (" ", end='')
    for x in range (dimensoes):
        print ("", x+1, end='')
    print()

def check(y, x, tabuleiro, dimensoes):
    if not (0 <= y < dimensoes) or not (0 <= x < dimensoes):
        return True

    if tabuleiro[y][x] in ("X", 0):
        return True

    return False


def ler_user_jogada(text, tabuleiro, dimensoes):
    while True:
        try:
            x, y = input(text).split()
            x, y = int(x)-1, ord(y.upper())-65
            if check(y, x, tabuleiro, dimensoes):
                raise Exception
            return [y, x]
        except:
            print ("INAVELIDO")

def ler_maq_jogada(tabuleiro, dimensoes):
    while True:
        y, x = randint(0, dimensoes-1), randint(0, dimensoes-1)
        if not check(y, x, tabuleiro, dimensoes):
            return [y, x]

def jogada (y, x, tabuleiro):
    if tabuleiro[y][x] == 1:
        tabuleiro[y][x] = 'X'
        return 1
    tabuleiro[y][x] = 0
    return 0

def user_jogada(tabuleiro, dimensoes):
    y, x = ler_user_jogada("Sua jogada: ", tabuleiro, dimensoes)
    return jogada(y, x, tabuleiro)

def maq_jogada(tabuleiro, dimensoes):
    y, x = ler_maq_jogada(tabuleiro, dimensoes)
    return jogada(y, x, tabuleiro)


def jogar(user, maquina, dimensoes, letras):
    Upt, Mpt = 0, 0
    while True:
        mostrar_tabuleiro(user, 0, dimensoes, letras)
        mostrar_tabuleiro(maquina, 1, dimensoes, letras)
        Upt += user_jogada(maquina, dimensoes)
        Mpt += maq_jogada(user, dimensoes)

        if Upt == dimensoes:
            return True
        if Mpt == dimensoes:
            return False

def main():
    dimensoes = 5
    user = inicializar_tabuleiro(dimensoes)
    maquina = inicializar_tabuleiro(dimensoes)
    letras = [chr(i+65) for i in range(dimensoes)]
    while True:
        match input("Escolha:\n\n1) Jogar\n2) Sair\n\n"):
            case "1":
                if jogar(user, maquina, dimensoes, letras):
                    print ("VOCÊ GANHOU!")
                else:
                    print ("VOCÊ PERDEU!")
            case "2":
                break
            case _:
                print ("Erro")

main()