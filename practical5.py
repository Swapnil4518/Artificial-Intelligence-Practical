AI = "X"
HUMAN = "O"
EMPTY = "_"


# Print board
def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check winner
def winner(board, player):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in lines
    )


# Check game end
def terminal(board):
    return winner(board, AI) or winner(board, HUMAN) or EMPTY not in board


# Calculate score
def utility(board):
    if winner(board, AI):
        return 1

    if winner(board, HUMAN):
        return -1

    return 0


# Minimax algorithm
def minimax(board, maximizing):

    if terminal(board):
        return utility(board)

    # AI MAX
    if maximizing:
        best = -float("inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI

                value = minimax(board, False)

                board[i] = EMPTY

                best = max(best, value)

        return best

    # Human MIN
    else:
        best = float("inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN

                value = minimax(board, True)

                board[i] = EMPTY

                best = min(best, value)

        return best


# Find best move
def best_move(board):
    best_value = -float("inf")
    move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI

            value = minimax(board, False)

            board[i] = EMPTY

            if value > best_value:
                best_value = value
                move = i

    return move


# Start game
def play_game():
    board = [EMPTY] * 9

    print("===== Minimax Tic-Tac-Toe =====")
    print("AI = X, Human = O")

    while True:

        # AI move
        print_board(board)
        move = best_move(board)

        if move is not None:
            board[move] = AI

        if winner(board, AI):
            print_board(board)
            print("AI wins!")
            break

        if EMPTY not in board:
            print_board(board)
            print("Game is a draw!")
            break

        # Human move
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1

                if 0 <= position < 9 and board[position] == EMPTY:
                    board[position] = HUMAN
                    break

                print("Invalid move. Try again.")

            except ValueError:
                print("Enter a number from 1 to 9.")

        if winner(board, HUMAN):
            print_board(board)
            print("Human wins!")
            break

        if EMPTY not in board:
            print_board(board)
            print("Game is a draw!")
            break


# Run game
play_game()