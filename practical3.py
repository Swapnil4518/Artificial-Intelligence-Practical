import math

def print_board(board):
    for i in range(0, 9, 3):
        print(" ".join(board[i:i+3]))
    print()


def check_winner(board):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != "_":
            return board[a]

    if "_" not in board:
        return "Draw"

    return None


def alpha_beta(board, alpha, beta, is_maximizing, nodes):
    nodes[0] += 1

    result = check_winner(board)

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if is_maximizing:
        max_eval = -math.inf

        for i in range(9):
            if board[i] == "_":
                board[i] = "X"

                score = alpha_beta(
                    board, alpha, beta, False, nodes
                )

                board[i] = "_"

                max_eval = max(max_eval, score)
                alpha = max(alpha, score)

                if beta <= alpha:
                    break

        return max_eval

    else:
        min_eval = math.inf

        for i in range(9):
            if board[i] == "_":
                board[i] = "O"

                score = alpha_beta(
                    board, alpha, beta, True, nodes
                )

                board[i] = "_"

                min_eval = min(min_eval, score)
                beta = min(beta, score)

                if beta <= alpha:
                    break

        return min_eval


def best_move(board):
    best_score = -math.inf
    move = -1
    nodes = [0]

    for i in range(9):
        if board[i] == "_":

            board[i] = "X"

            score = alpha_beta(
                board,
                -math.inf,
                math.inf,
                False,
                nodes
            )

            board[i] = "_"

            if score > best_score:
                best_score = score
                move = i

    return move, nodes[0]


print("========== Alpha-Beta Pruning for Tic-Tac-Toe ==========")

board = ["_"] * 9

print("Initial Board:")
print_board(board)

# AI first move
move, nodes_evaluated = best_move(board)

board[move] = "X"

print("AI (X) chooses position:", move)
print("Nodes evaluated:", nodes_evaluated)

print("Board after AI move:")
print_board(board)


# Human move
board[4] = "O"

print("Human (O) plays center (position 4)")
print_board(board)


# AI second move
move, nodes_evaluated = best_move(board)

board[move] = "X"

print("AI (X) chooses position:", move)
print("Nodes evaluated:", nodes_evaluated)

print("Board after AI move:")
print_board(board)