import math

# Função para imprimir o tabuleiro do jogo da velha
def imprimir_tabuleiro(tabuleiro):
    # Itera sobre as linhas do tabuleiro
    for i, linha in enumerate(tabuleiro):
        # Imprime os elementos da linha separados por "|" e adiciona espaços
        print(" " + " | ".join(linha))
        # Adiciona linha separadora entre as linhas do tabuleiro, exceto na última
        if i < 2:
            print("---|---|---")

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verifica se algum jogador venceu nas linhas, colunas ou diagonais
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    # Verifica se todas as células do tabuleiro estão preenchidas
    return all(celula != " " for linha in tabuleiro for celula in linha)

# Algoritmo Minimax para a IA
def minimax(tabuleiro, profundidade, is_maximizing):
    # Verifica se há vitória ou empate
    if verificar_vitoria(tabuleiro, "X"):
        return -10 + profundidade
    elif verificar_vitoria(tabuleiro, "O"):
        return 10 - profundidade
    elif verificar_empate(tabuleiro):
        return 0

    # Lógica do algoritmo Minimax
    if is_maximizing:
        melhor_valor = -math.inf
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "O"
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[linha][coluna] = " "
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = math.inf
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "X"
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[linha][coluna] = " "
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para a IA fazer a jogada
def fazer_jogada(tabuleiro):
    melhor_valor = -math.inf
    melhor_jogada = None
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "O"
                valor = minimax(tabuleiro, 0, False)
                tabuleiro[linha][coluna] = " "
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (linha, coluna)
    return melhor_jogada

# Função principal para jogar o jogo da velha
def jogar_jogo_da_velha():
    # Inicializa o tabuleiro do jogo
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador_atual = "O"

    # Pede ao jogador que escolha o modo de jogo
    modo_de_jogo = input("Escolha o modo de jogo:\n1 - Jogador vs Jogador\n2 - Jogador vs IA\n")

    # Loop principal do jogo
    while True:
        # Imprime o tabuleiro atual
        imprimir_tabuleiro(tabuleiro)

        # Verifica o modo de jogo escolhido
        if modo_de_jogo == "1":  # Se escolheu modo Jogador vs Jogador
            # Jogador atual faz sua jogada
            linha = int(input("Jogador {}, escolha a linha (0, 1, 2): ".format(jogador_atual)))
            coluna = int(input("Jogador {}, escolha a coluna (0, 1, 2): ".format(jogador_atual)))
            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada. Escolha outra.")
                continue
            tabuleiro[linha][coluna] = jogador_atual
        else:  # Se escolheu modo Jogador vs IA
            if jogador_atual == "X":  # Jogador humano
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))
                if tabuleiro[linha][coluna] != " ":
                    print("Essa posição já está ocupada. Escolha outra.")
                    continue
                tabuleiro[linha][coluna] = jogador_atual
            else:  # IA
                linha, coluna = fazer_jogada(tabuleiro)
                tabuleiro[linha][coluna] = jogador_atual

        # Verifica se o jogo acabou
        if verificar_vitoria(tabuleiro, jogador_atual):
            # Se um jogador venceu, exibe a mensagem de vitória e encerra o jogo
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        elif verificar_empate(tabuleiro):
            # Se o jogo empatou, exibe a mensagem de empate e encerra o jogo
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        # Alterna o jogador atual
        jogador_atual = "X" if jogador_atual == "O" else "O"

# Inicia o jogo da velha
jogar_jogo_da_velha()
