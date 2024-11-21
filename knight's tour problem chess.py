def is_valid_move(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def solve_knight_tour(x, y, move_count, board, moves_x, moves_y, n):
    if move_count == n * n:
        return True

    for i in range(8):
        next_x = x + moves_x[i]
        next_y = y + moves_y[i]
        if is_valid_move(next_x, next_y, board, n):
            board[next_x][next_y] = move_count
            if solve_knight_tour(next_x, next_y, move_count + 1, board, moves_x, moves_y, n):
                return True

            board[next_x][next_y] = -1

    return False

def knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    if solve_knight_tour(0, 0, 1, board, moves_x, moves_y, n):
        print("Knight's Tour solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists.")
        
try:
    n = int(input("Enter the size of the chessboard (NxN): "))
    if n < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        knight_tour(n)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
