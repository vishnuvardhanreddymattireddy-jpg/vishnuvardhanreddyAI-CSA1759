# Minimax for Tic Tac Toe

board = [' ']*9

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def minimax(is_max):
    if check_winner('O'): return 1
    if check_winner('X'): return -1
    if ' ' not in board: return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_val = -100
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Game Loop (Player vs AI)
while True:
    print_board()
    
    # Player Move
    player = int(input("Enter position (1-9): ")) - 1
    if board[player] != ' ':
        print("Invalid move!")
        continue
    board[player] = 'X'
    
    if check_winner('X'):
        print_board()
        print("Player Wins!")
        break
    if ' ' not in board:
        print_board()
        print("Draw!")
        break
    
    # AI Move
    ai = best_move()
    board[ai] = 'O'
    
    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break
    if ' ' not in board:
        print_board()
        print("Draw!")
        break
