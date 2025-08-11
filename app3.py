#python
# Jogo da Velha (Tic Tac Toe) em Python

# Tabuleiro representado por uma lista de 9 posições (inicialmente vazias)
board = [' ' for _ in range(9)]

def print_board():
    """
    Exibe o tabuleiro atual formatado com as marcações dos jogadores
    Formato:
    | X | O | X |
    | O | X | O |
    | X | O | X |
    """
    # Cria cada linha do tabuleiro usando formatação de string
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    # Exibe o tabuleiro completo
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    """
    Gerencia a jogada de um participante
    :para icon: 'X' ou 'O' - símbolo do jogador atual
    """
    # Determina o número do jogador baseado no símbolo
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Sua vez, jogador {}".format(number))
    
    # Loop para entrada válida da jogada
    while True:
        try:
            # Converte a entrada para número e ajusta para índice 0-8
            choice = int(input("Digite sua jogada (1-9): ").strip()) - 1
            
            # Valida se a posição está disponível
            if board[choice] == ' ':
                board[choice] = icon
                break
            else:
                print("\nEsta posição já está ocupada!")
        except (ValueError, IndexError):
            print("\nEntrada inválida! Digite um número entre 1 e 9.")

def is_victory(icon):
    """
    Verifica se o jogador atual venceu
    :param icon: 'X' ou 'O' - símbolo a ser verificado
    :return: True se houver vitória, False caso contrário
    """
    # Verifica todas as combinações vencedoras possíveis
    return (
        # Vitórias horizontais
        (board[0] == icon and board[1] == icon and board[2] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        
        # Vitórias verticais
        (board[0] == icon and board[3] == icon and board[6] == icon) or
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        
print("Último elemento:", array[-1])

        # Vitórias diagonais
        (board[0] == icon and board[4] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon)
    )

# Loop principal do jogo
while True:
    # Jogador X (1) faz sua jogada
    print_board()
    player_move('X')
    
    # Verifica vitória do X ou empate
    if is_victory('X'):
        print_board()
        print("Jogador 1 (X) venceu! Parabéns!")
        break
    elif ' ' not in board:  # Todas posições preenchidas
        print_board()
        print("Empate!")
        break
    
    # Jogador O (2) faz sua jogada
    print_board()
    player_move('O')
    
    # Verifica vitória do O
    if is_victory('O'):
        print_board()
        print("Jogador 2 (O) venceu! Parabéns!")
        break