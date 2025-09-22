#Defining the game board
game_board = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}
#displaying the board
def print_game_board():
    print(f"{game_board["A1"]}|{game_board["A2"]}|{game_board["A3"]}")
    print("-+-+-")
    print(f"{game_board["B1"]}|{game_board["B2"]}|{game_board["B3"]}")
    print("-+-+-")
    print(f"{game_board["C1"]}|{game_board["C2"]}|{game_board["C3"]}")
    print("-+-+-")
 #checking for a win
def check_win(player):
    win_combinations = [
        ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],  # rows
        ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],  # columns
        ["A1", "B2", "C3"], ["A3", "B2", "C1"]                       # diagonals
    ]
    return any(all(game_board[pos] == player for pos in combinations) for combinations in win_combinations)
#checking for a tie
def check_if_tie():
    return all(space != " " for space in game_board.values())
#player move
def player_move():
    while True:
        move = input("Your move (A1–C3): ").upper()
        if move in game_board:
            if game_board[move] == " ":
                game_board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        else:
            print("Invalid position. Try again.")
#AI move
def ai_move():
    for key in game_board:
        if game_board[key] == " ":
            game_board[key] = "O"
            if check_win("O"):
                return
            game_board[key] = " "
    for key in game_board:
        if game_board[key] == " ":
            game_board[key] = "X"
            if check_win("X"):
                game_board[key] = "O"
                return
            game_board[key] = " "
    for key in game_board:
        if game_board[key] == " ":
            game_board[key] = "O"
            return
#playing main game
def main():
    while True:
        print_game_board()
        player_move()
        if check_win("X"):
            print_game_board()
            print("You win!")
            break
        if check_if_tie():
            print_game_board()
            print("It's a tie!")
            break
        ai_move()
        if check_win("0"):
            print_game_board()
            print("You Lose!")
            break
        if check_if_tie():
            print_game_board()
            print("It's a tie!")
            break
#starting the game
main()


    
