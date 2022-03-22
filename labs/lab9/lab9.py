"""
Name: <Kate Culpepper>
<Lab9>.py

This program allows the user to play a game of tic tac toe
"""


def build_board():  # list of elements 1-9 and re
    game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return game_list


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    board[position - 1] = character.strip().lower()


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    no_moves = False
    for i in board:
        if i == 'x' or i == 'o':
            no_moves = True
        else:
            no_moves = False
            break
    if winning_game(board) == True:
        return True
    elif no_moves == True:
        return True
    else:
        return False


def get_winner(board):
    if winning_game(board) == True and game_over(board) :

        if board[0] == board[1] == board[2] == 'x':
            return 'x'
        elif board[0] == board[3] == board[6]  == 'x':
            return 'x'
        elif board[1] == board[4] == board[7] == 'x':
            return 'x'
        elif board[2] == board[5] == board[8] == 'x':
            return 'x'
        elif board[3] == board[4] == board[5] == 'x':
            return 'x'
        elif board[6] == board[7] == board[8] == 'x':
            return 'x'
        elif board[0] == board[4] == board[8] == 'x':
            return 'x'
        elif board[2] == board[4] == board[6] == 'x':
            return 'x'
        else:
            return 'o'
    else:
        return None

def play(board):
    user_instructions = "Let's Play Tic Tac Toe! X's go first, to choose your position choose a number 1-9"
    print(user_instructions)
    print_board(board)
    while winning_game(board) == False and game_over(board) == False:
        input_x = eval(input("X's, choose a position:"))
        if is_legal(board, input_x):
            fill_spot(board, input_x, 'x')
            print_board(board)
            if game_over(board):
                break
        else:
            print("That's illegal!")
        input_o = eval(input("o's, choose a position:"))
        if is_legal(board, input_o):
            fill_spot(board, input_o, 'o')
            print_board(board)
            if game_over(board):
                break
        else:
            print("That's illegal!")
    if get_winner(board) == 'x':
        print("x's win!")
    elif get_winner(board) == 'o':
        print("O's win!")
    else:
        print("It's a tie!")
    replay_input = input("Play again?")

    if replay_input[0] == 'y':

        main()


def main():
    play(build_board())



if __name__ == '__main__':


    main()
