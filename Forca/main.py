from random import randint

def fill(palavra, Len, adivinha):
    for letra in palavra:
        if letra == " ":
            adivinha.append("-")
            Len -= 1
        else:
            adivinha.append("_")
    return Len

def mapear(palavra):
    mapa = {}
    boolean = [False]*26
    for i, letra in enumerate(palavra):
        if letra != " " and letra != "-":
            intLetra = ord(letra)-65
            if (not boolean[intLetra]):
                mapa[letra] = [i]
                boolean[intLetra] = True
            else:
                mapa[letra].append(i)
    return mapa

def mostrar_tentadas(tentadas):
    print ("\nTENTADAS")
    for i, letra in enumerate(tentadas):
        if letra:
            print (chr(i+65), "", end='')
        if i+1 % 5 == 0:
            print ()
    print("\n")

def jogar(palavra, tema):
    Len = len(palavra)
    mapa = mapear(palavra)
    adivinha = []
    Len = fill(palavra, Len, adivinha)
    tentadas = [False]*26
    rep = [0]*26
    for i in mapa:
        rep[ord(i)-65] = 1
    pt, tent = 0, 0
    while tent != Len:
        if (pt == Len):
            print ("\n", palavra, "\nVoce ganhou")
            return True
        mostrar_tentadas(tentadas)
        print (tema)
        for let in adivinha:
            print (let, end='')
        let = input("\n").upper()
        intLet = ord(let)-65
        if rep[intLet] == 1:
            rep[intLet] = 2
            for i in mapa[let]:
                adivinha[i] = let
                pt += 1
        elif rep[intLet] == 0:
            tentadas[intLet] = 1
            tent += 1
            rep[intLet] = 2
        else:
            print("\nLetra já escolhida")
    print ("\nVocê perdeu.\nA palavra era", palavra)
    return False

def selecionar_palavra():
    temas = ["Animais", "Filmes famosos", "Esportes", "Países", "Comidas", "Personagens de desenhos animados", "Objetos do dia a dia"]
    tema = randint(0, 6)
    rand = randint(1, 50)
    with open ("Forca/palavras.txt", "r", encoding="utf-8") as palavras:
        palavra = palavras.readlines()[52*(tema)+rand]
    
    jogar(palavra.upper().rstrip("\n"), temas[tema])

selecionar_palavra()