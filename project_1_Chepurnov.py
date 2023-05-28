from random import randrange


def display_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("---------")


def enter_move(board):
    free_fields = make_list_of_free_fields(board)

    if len(free_fields) == 0:
        return

    valid_input = False
    while not valid_input:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move)
            if move in free_fields:
                valid_input = True
                update_board(board, move, "O")
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if str(board[row][col]).isdigit():
                free_fields.append(board[row][col])
    return free_fields


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def update_board(board, move, sign):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == move:
                board[row][col] = sign


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = randrange(1, 10)
    while move not in free_fields:
        move = randrange(1, 10)
    update_board(board, move, "X")


def play_game():
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("You win!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            if not victory_for(board, "X"):
                print("It's a tie!")
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("Computer wins!")
            break


play_game()