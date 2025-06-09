from random import randint

perguntas = [
    "Qual é o valor de π (pi) arredondado para duas casas decimais?",
    "Qual é a derivada de x²?",
    "Qual é a solução da equação 2x + 3 = 7?",
    "Qual é a soma dos ângulos internos de um triângulo?",
    "Qual é o próximo número na sequência: 2, 4, 8, 16, ___?",
    "Quanto é √144?",
    "Em um triângulo retângulo, o seno de 30° é:",
    "Qual é a fórmula da área de um círculo?",
    "Qual número é primo?",
    "Quanto é 2⁵?",
    "Qual é a média dos números 3, 5, 7 e 9?",
    "Um ângulo reto tem quantos graus?]"
    "O que é um número irracional?",
    "O logaritmo de 100 na base 10 é:",
    "Qual é a fórmula do teorema de Pitágoras?",
    "O número 0 é considerado:",
    "O determinante da matriz [1 2; 3 4] é:",
    "Qual é o valor absoluto de -15?",
    "Um decágono possui quantos lados?",
    "O fatorial de 4 (4!) é:",
    "Um número dividido por zero é:",
    "A equação x² + 4x + 4 = 0 tem:",
    "A função f(x) = 2x + 3 é:",
    "O número de Euler (e) é aproximadamente:",
    "Qual é a raiz cúbica de 27?"
    ]
alternativas = [
    "A) 3,12   B) 3,14   C) 3,16   D) 3,18   E) 3,10",
    "A) 1      B) x      C) 2x     D) x²     E) 0",
    "A) 1      B) 2      C) 3      D) 4      E) 5",
    "A) 90°    B) 180°   C) 270°   D) 360°   E) 45°",
    "A) 18     B) 20     C) 24     D) 30     E) 32",
    "A) 10     B) 11     C) 12     D) 13     E) 14",
    "A) 0      B) 0,5    C) 1      D) √2/2   E) √3/2",
    "A) πr²    B) 2πr    C) πd     D) 2rπ²   E) r²π²",
    "A) 4      B) 6      C) 9      D) 11     E) 15",
    "A) 16     B) 24     C) 32     D) 64     E) 128",
    "A) 5      B) 6      C) 7      D) 8      E) 9",
    "A) 30°    B) 45°    C) 60°    D) 90°    E) 180°",
    "A) Que não é divisível por 2\nB) Que é negativo\nC) Que não pode ser expresso como fração\nD) Que é maior que 100\nE) Que tem parte imaginária",
    "A) 1      B) 2      C) 10     D) 100    E) 0",
    "A) a + b = c\nB) a² + b² = c²\nC) ab = c\nD) a² = b² + c²\nE) a + b + c = 180",
    "A) Primo   B) Par   C) Ímpar   D) Negativo   E) Imaginário",
    "A) -2      B) -1     C) 0      D) 1      E) 2",
    "A) -15     B) 0      C) 15     D) 30     E) 1",
    "A) 12      B) 16     C) 20     D) 24     E) 30",
    "A) 6       B) 8      C) 10     D) 12     E) 14",
    "A) Zero    B) Infinito   C) Indeterminado   D) O próprio número   E) Negativo",
    "A) Duas raízes reais e distintas\nB) Uma raiz real dupla\nC) Nenhuma raiz real\nD) Duas raízes imaginárias\nE) Três raízes",
    "A) Linear   B) Quadrática   C) Exponencial   D) Logarítmica   E) Constante",
    "A) 2,14     B) 2,28     C) 2,71     D) 3,14     E) 3,71",
    "A) 2        B) 3        C) 4        D) 5        E) 6",
]
gabarito = [
    "B",
    "C",
    "B",
    "B",
    "E",
    "C",
    "B",
    "A",
    "D",
    "C",
    "B",
    "D",
    "C",
    "B",
    "B",
    "B",
    "A",
    "C",
    "C",
    "D",
    "C",
    "B",
    "A",
    "C",
    "B",
]

def jogar(perguntas, alternativas, gabarito):
    quiz = []
    alts = []
    gaba = []
    n = 0
    memo = [False]*25
    while n < 10:
        rand = randint(0, 24)
        if not memo[rand]:
            n += 1
            quiz.append(perguntas[n])
            alts.append(alternativas[n])
            gaba.append(gabarito[n])
            memo[rand] = True
    points = 0
    for i in range(10):
        print ("PONTUAÇÃO:", points)
        ans = input(f"{quiz[i]}\n{alts[i]}\n")
        if ans == gaba[i]:
            points += 1
            print ("\nCORRETO\n")
        else:
            print ("\nERRADO\n")
    print ("PONTUAÇÃO:", points)

while True:
    match input("Escolha:\n\n1) Jogar\n2) Sair\n\n"):
        case "1":
            jogar(perguntas, alternativas, gabarito)
        case "2":
            break
        case _:
            print ("Erro")