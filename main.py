import random
import copy

def printTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if(i < 2):
            print("------")

# def verificaGanhador(tabuleiro):
#     # Linhas
#     for i in range(3):
#         if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " "):  # Linhas horizontais
#             return tabuleiro[i][0]

#     # Colunas
#     for i in range(3):
#         if (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " "):  # Colunas verticais
#             return tabuleiro[0][i]

#     # Diagonais
#     if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " "):  # Diagonal principal
#         return tabuleiro[0][0]
#     if (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " "):  # Diagonal secundária
#         return tabuleiro[0][2]

#     # Verifica o formato de "L"
#     if (tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[1][1] != " " and
#             tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != " "):  # Formato de "L" para X
#         return tabuleiro[1][1]
#     elif (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[1][1] != " " and
#           tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != " "):  # Formato de "L" para X
#         return tabuleiro[1][1]
#     elif (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][0] != " " and
#           tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[1][0] != " "):  # Formato de "L" para O
#         return tabuleiro[1][1]
#     elif (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][0] != " " and
#           tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[2][1] != " "):  # Formato de "L" para O
#         return tabuleiro[1][1]

#     for i in range(3):
#         for j in range(3):
#             if tabuleiro[i][j] == " ":
#                 return False

#     return "EMPATE"   [i, j] not in bloqueados and 

def verificaGanhador(tabuleiro):
    # linhas 
    for i in range(3):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " "):
            return tabuleiro[i][0]
    
    # coluna
    for i in range(3):
        if(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " "):
            return tabuleiro[0][i]

    # diagonal principal
    if(tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]

    # diagonal secundaria
    if(tabuleiro[0][2] != " " and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == " "):
                return False

    return "EMPATE"

def acoes(tabuleiro, bloqueados):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                posicoes.append([i,j])
    return posicoes

def fazerjogada(tabuleiro,posicao,jogador):
    novoTabuleiro = copy.deepcopy(tabuleiro)
    novoTabuleiro[posicao[0]][posicao[1]] = simbolo[jogador]
    return novoTabuleiro

def minimax(tabuleiro, jogador, score):
    ganhador = verificaGanhador(tabuleiro)
    if ganhador:
        return score[ganhador]

    jogadas = acoes(tabuleiro,bloqueados)

    if jogador == 0:   # MAX
        melhorValor = float('-inf')  # Inicialize com o valor mínimo possível
        for jogada in jogadas:
            aux = fazerjogada(tabuleiro,jogada,jogador)
            jogador = (jogador + 1) % 2
            valor = minimax(aux, jogador, score)
            melhorValor = max(melhorValor, valor)
        return melhorValor
    else:               # MIN
        melhorValor = float('inf')  # Inicialize com o valor máximo possível
        for jogada in jogadas:
            aux = fazerjogada(tabuleiro,jogada,jogador)
            jogador = (jogador + 1) % 2
            valor = minimax(aux, jogador, score)
            melhorValor = min(melhorValor, valor)
        return melhorValor

def bot(tabuleiro, jogador, simbolo, bloqueados):
    jogadas = acoes(tabuleiro, bloqueados)
    melhorValor = 0
    melhorMovimento = 0
    score = {"EMPATE": 0, "X": 1, "O": -1}
    for jogada in jogadas:
        aux = fazerjogada(tabuleiro,jogada,jogador)
        jogador = (jogador + 1) % 2
        valor = minimax(aux, jogador, score)
        if melhorValor == 0:
            melhorValor = valor
            melhorMovimento = jogada
        elif(jogador==0):
            if(valor > melhorValor):
                melhorValor = valor
                melhorMovimento = jogada
        elif(jogador==1):
            if(valor < melhorValor):
                melhorValor = valor
                melhorMovimento = jogada

            
    return melhorMovimento[0], melhorMovimento[1]

if __name__ == "__main__":
    tabuleiro = [       # Define o tabuleiro
        [" "," ", " "],
        [" "," ", " "],
        [" "," ", " "],
    ]
    simbolo = ["X","O"] # Define o símbolo para o jogador
    jogador = 1        # 0 para o primeiro jogador, 1 para o segundo jogador
    ganhador = verificaGanhador(tabuleiro)
    
    # Bloquear dois espaços aleatórios
    bloqueados = []
    # for _ in range(2):
    #     i, j = random.randint(0, 2), random.randint(0, 2)
    #     bloqueados.append([i, j])
    
    while not ganhador:
        printTabuleiro(tabuleiro)
        if jogador == 0:   # Primeiro jogador
            i, j = bot(tabuleiro, jogador, simbolo, bloqueados)
            print("\nPrimeiro Jogador")
        else:               # Segundo jogador
            i = int(input("Linha: "))
            j = int(input("Coluna: "))
            print("\nSegundo Jogador")
            
        if [i, j] not in bloqueados:
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = simbolo[jogador]
                jogador = (jogador + 1) % 2
            else:
                print("Posição já está ocupada")
        else:
            print("Esta posição está bloqueada.")

        ganhador = verificaGanhador(tabuleiro)

    printTabuleiro(tabuleiro)
    print("Resultado: ", ganhador, "\n")


