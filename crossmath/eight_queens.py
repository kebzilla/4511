import timeit

def initialize_board(d):
    board =[]
    for i in range(0, d):
        board.insert(i, list(range((i *d) + 1, ((i + 1) * d) + 1)))
    return board

def initialize_board1D(d):
    d = d * d
    board = list(range(1, d + 1))
    return board

def print_board(board, d):
    for i in range (0, d):
        print(board[i])
    print()

def queen_attack(board, x, y, d):
    for i in range(0, 6):
        if board[i][y] == 0:
            board[i][y] = 1
        if board[i - y - 1][y] == 0:
            board[i - y - 1][y] = 1
    for j in range(0, 6):
        if board[x][j] == 0:
            board[x][j] = 1
        if board[x][j - x - 1] == 0:
            board[x][j - x - 1] = 1

def update_attacks(board, d):
    for i in range(0, d):
        for j in range(0, d):
            if board[i][j] == 'Q':
                queen_attack(board, i, j, d)

def test1(d):
    begin = timeit.default_timer()
    board = initialize_board1D(d)
    end = timeit.default_timer()
    print("initialize 1D:", end - begin)
    print(board)

def test2(d):
    start = timeit.default_timer()
    board = initialize_board(d)
    stop = timeit.default_timer()
    print("initialize 2D:", stop - start)
    print(board)

test1(5)
test2(5)
