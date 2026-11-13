def check(a, b, c):
    """Return True if the three cells are the same and not empty."""
    return a == b == c and a in ('X', 'O')


def is_win(game):
    # rows
    if check(game[0][0], game[0][1], game[0][2]):
        return True
    if check(game[1][0], game[1][1], game[1][2]):
        return True
    if check(game[2][0], game[2][1], game[2][2]):
        return True
    # columns
    if check(game[0][0], game[1][0], game[2][0]):
        return True
    if check(game[0][1], game[1][1], game[2][1]):
        return True
    if check(game[0][2], game[1][2], game[2][2]):
        return True
    # diagonals
    if check(game[0][0], game[1][1], game[2][2]):
        return True
    if check(game[0][2], game[1][1], game[2][0]):
        return True
    return False


def main():
    # Initialize the game board
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player1 = 'X'
    player2 = 'O'
    # False = player 1's turn, True = player 2's turn; player 1 moves first.
    turn = True
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # toggle turn
        if turn == False:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        # Read and validate the cell; keep asking on the same turn until valid.
        while True:
            try:
                i, j = map(int, input("Which cell? i: [1..3], j: [1..3]: ").split())
            except ValueError:
                print("Please enter two integers.")
                continue
            if not (1 <= i <= 3 and 1 <= j <= 3):
                print("Out of range: i and j must be 1..3.")
                continue
            if game[i - 1][j - 1] != ' ':
                print("That cell is already taken.")
                continue
            break
        if turn == False:
            game[i - 1][j - 1] = 'X'
        else:
            game[i - 1][j - 1] = 'O'
        if is_win(game):
            print("Win!")
            break
        if n == 8:  # all 9 cells have been filled
            print("Tie!")
        # Show the board
        print(game[0][0] + " " + game[0][1] + " " + game[0][2])
        print(game[1][0] + " " + game[1][1] + " " + game[1][2])
        print(game[2][0] + " " + game[2][1] + " " + game[2][2])


if __name__ == "__main__":
    main()
