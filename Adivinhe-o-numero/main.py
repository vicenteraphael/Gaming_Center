from random import randint

def tentativa(tent, num):
    cnt = 0
    while tent != cnt:
        cnt += 1
        palp = int(input("\nNº: "))
        if (palp < num):
            print ("ERRADO! O NÚMERO SORTEADO É MAIOR")
        elif (palp > num):
            print ("ERRADO! O NÚMERO SORTEADO É MENOR")
        else:
            return True
        print (f"TENTATIVAS: {cnt}/{tent}")

def jogar():
    match input("ESCOLHA A DIFICULDADE:\n\n1) Fácil (1 a 100), 10 tentativas\n2) Médio (1 a 500), 15 tentativas\n3) Difícil (1 a 1000), 20 tentativas\n\n"):
        case "1":
            tent = 10
            rand = randint(1, 100)
        case "2":
            tent = 15
            rand = randint(1, 500)
        case "3":
            tent = 20
            rand = randint(1, 1000)
        case _:
            print ("Erro")
    print ("\nVOCÊ GANHOU, PARABÉNS!") if tentativa(tent, rand) else print ("\nVOCÊ PERDEU, OTÁRIO!\n\no número era:", rand)
    

while True:
    match input("Desejas:\n\n1) Jogar\n2) Sair\n\n"):
        case "1":
            jogar()
        case "2":
            break
        case _:
            print ("Erro")
