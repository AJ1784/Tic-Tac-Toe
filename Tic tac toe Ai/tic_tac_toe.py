def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def player_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])


def minimax(board, depth, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player):
        return 1
    elif check_win(board, human_player):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai_player
                    score = minimax(board, depth + 1, False, ai_player, human_player)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = human_player
                    score = minimax(board, depth + 1, True, ai_player, human_player)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


def ai_move(board, ai_player, human_player):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai_player
                score = minimax(board, 0, False, ai_player, human_player)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = ai_player


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    ai_player = 'O'

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if player_move(board, row, col, player):
            if check_win(board, player):
                print_board(board)
                print("Player X wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            ai_move(board, ai_player, player)
            if check_win(board, ai_player):
                print_board(board)
                print("AI wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()