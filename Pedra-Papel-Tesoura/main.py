from random import randint

def jogo():
    #0: pedra, 1: papel, 2: tesoura
    
    frase = ["JÓ", "KEN"]
    for silaba in frase:
        input(f"{silaba}\nPRESSIONE ENTER")

    escolhas = ["🪨", "📃", "✂️"]

    usuario = randint(0, 2)
    maquina = randint(0, 2)
    print (f"PÔ\n\nVOCÊ | Máquina\n{escolhas[usuario]}   vs.  {escolhas[maquina]}\n")

    if ((usuario == 0 and maquina == 2) or (usuario == 1 and maquina == 0) or (usuario == 2 and maquina == 1)):
        return 0
    elif (usuario == maquina):
        return 1
    return False

while True:
    match input("Escolha:\n\n1) Jogar\n2) Sair\n\n"):
        case "1":
            match jogo():
                case 0:
                    print ("VOCÊ GANHOU!\n")
                case 1:
                    print ("Empate!\n")
                case 2:
                    print ("VOCÊ PERDEU!\n")
            input("PRESSIONE ENTER")
            print()
        case "2":
            break
        case _:
            print ("Erro")