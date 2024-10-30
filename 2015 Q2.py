import numpy as np
r = 0
a, c, m = map(int, input().split())
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
board = np.zeros((10, 10), dtype=int)

for ship in ships:
    valid = False
    while valid == False:
        r = (a * r + c) % m
        if r < 10:
            y_coordinate = 0
            x_coordinate = r
        else:
            y_coordinate = (r // 10) % 10
            x_coordinate = r % 10

        r = (a * r + c) % m
        valid = True
        if r % 2 == 0:
            if x_coordinate + ship - 1 > 9:
                valid = False
            else:
                for i in range(ship):
                    if board[y_coordinate][x_coordinate + i] > 0:
                        valid = False
                        break
                    if y_coordinate > 0 and board[y_coordinate - 1][x_coordinate + i] > 0:
                        valid = False
                        break
                    if y_coordinate < 9 and board[y_coordinate + 1][x_coordinate + i] > 0:
                        valid = False
                        break
                if valid == True and x_coordinate > 0 and board[y_coordinate][x_coordinate - 1] > 0:
                    valid = False
                if valid == True and x_coordinate + ship -1 < 9 and board[y_coordinate][x_coordinate + ship] > 0:
                    valid = False
                if valid == True and y_coordinate > 0 and x_coordinate > 0 and board[y_coordinate - 1][x_coordinate - 1] > 0:
                    valid = False
                if valid == True and y_coordinate < 9 and x_coordinate > 0 and board[y_coordinate + 1][x_coordinate - 1] > 0:
                    valid = False
                if valid ==True and x_coordinate + ship -1 < 9 and y_coordinate < 9 and board[y_coordinate + 1][x_coordinate + ship] > 0:
                    valid = False
                if valid ==True and x_coordinate + ship -1 < 9 and y_coordinate < 9 and board[y_coordinate - 1][x_coordinate + ship] > 0:
                    valid = False
        else:
            if y_coordinate + ship - 1 > 9:
                valid = False
            else:
                for i in range(ship):
                    if board[y_coordinate + i][x_coordinate] > 0:
                        valid = False
                        break
                    if x_coordinate > 0 and board[y_coordinate + i][x_coordinate - 1] > 0:
                        valid = False
                        break
                    if x_coordinate < 9 and board[y_coordinate + i][x_coordinate + 1] > 0:
                        valid = False
                        break
                if valid and y_coordinate > 0 and board[y_coordinate - 1][x_coordinate] > 0:
                    valid = False
                if valid and y_coordinate + ship-1< 9 and board[y_coordinate + ship][x_coordinate] > 0:
                    valid = False
                if valid == True and x_coordinate > 0 and y_coordinate > 0 and board[y_coordinate - 1][x_coordinate - 1] > 0:
                    valid = False
                if valid == True and x_coordinate < 9 and y_coordinate > 0 and board[y_coordinate - 1][x_coordinate + 1] > 0:
                    valid = False
                if valid ==True and y_coordinate + ship -1 < 9 and x_coordinate < 9 and board[y_coordinate + ship][x_coordinate + 1] > 0:
                    valid = False
                if valid ==True and y_coordinate + ship -1 < 9 and x_coordinate < 9 and board[y_coordinate - ship][x_coordinate - 1] > 0:
                    valid = False
    if valid == True:
        if r % 2 == 0:
            for i in range(ship):
                board[y_coordinate][x_coordinate + i] = 1
            print(f"{x_coordinate} {y_coordinate} {'H'}")
        else:
            for i in range(ship):
                board[y_coordinate + i][x_coordinate] = 1
            print(f"{x_coordinate} {y_coordinate} {'V'}")

print(board)
