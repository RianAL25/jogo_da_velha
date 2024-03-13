def printTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if(i < 2):
            print("------")

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

#Mini Max
def acoes(tabuleiro):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j]==" "):
                posicoes.append([i,j])
    return posicoes

def minimax(tabuleiro, jogador,score):
    ganhador = verificaGanhador(tabuleiro)
    if(ganhador):
        return score[ganhador]
    jogadas = acoes(tabuleiro)
    
    if(jogador == 0):   #MAX
        melhorValor = 0
        for jogada in jogadas:
            tabuleiro[jogada[0]][jogada[1]] = simbolo[jogador]
            jogador = (jogador + 1)%2
            valor = minimax(tabuleiro, jogador,score)
            tabuleiro[jogada[0]][jogada[1]] = " "
            if(valor>melhorValor):
                melhorValor = valor
        return melhorValor
    else:               #MIN
        melhorValor = 0
        for jogada in jogadas:
            tabuleiro[jogada[0]][jogada[1]] = simbolo[jogador]
            jogador = (jogador + 1)%2
            valor = minimax(tabuleiro, jogador,score)
            tabuleiro[jogada[0]][jogada[1]] = " "
            if(valor>melhorValor):
                melhorValor = valor
        return melhorValor

def bot(tabuleiro,jogador,simbolo):
    jogadas = acoes(tabuleiro)
    melhorValor = 0
    melhorMovimento = 0
    score = {"EMPATE": 0,"X": 1,"O": -1}
    for jogada in jogadas:
        tabuleiro[jogada[0]][jogada[1]] = simbolo[jogador]
        jogador = (jogador + 1)%2
        valor = minimax(tabuleiro, jogador,score)
        tabuleiro[jogada[0]][jogada[1]] = " "
        if(valor>melhorValor):
            melhorValor = valor
            melhorMovimento = jogada
            
    return melhorMovimento[0], melhorMovimento[1]

if(__name__ == "__main__"):
    tabuleiro = [       #define tabuleiro
        [" "," ", " "],
        [" "," ", " "],
        [" "," ", " "],
    ]
    simbolo = ["X","O"] #define o simbolo para o jogador
    jogador = 0         #0 primeiro jogador, 1 segundo jogador
    ganhador = verificaGanhador(tabuleiro)
    
    while(not ganhador):
        printTabuleiro(tabuleiro)
        if(jogador == 0):   #primeiro jogador
            i = int(input("Linha: "))
            j = int(input("Coluna: "))
            print("\nPrimeiro Jogador")
        else:               #segundo jogador
            i,j = bot(tabuleiro,jogador,simbolo)
            print("\nSegundo Jogador")
            
        if(tabuleiro[i][j] == " "):
            tabuleiro[i][j] = simbolo[jogador]
            jogador = (jogador+1)%2
        else:
            print("Posição já está ocupada")
        
        ganhador = verificaGanhador(tabuleiro)
    
    printTabuleiro(tabuleiro)
    print("Resultado: ",ganhador,"\n")
        
        