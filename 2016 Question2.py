import numpy as np

start_pos, sequence_length, steps = map(int, input().split())
sequence = input().split()
sequence = [int(i) for i in sequence]

grid = np.zeros((10, 10), dtype=int)
def migrate():
    migrates = np.all(grid <= 3)
    while not migrates:
        for y_coordinate in range(5):
            for x_coordinate in range(5):
                if grid[y_coordinate][x_coordinate] > 3:
                    grid[y_coordinate][x_coordinate] = 0
                    grid[y_coordinate + 1][x_coordinate] += 1
                    grid[y_coordinate][x_coordinate + 1] += 1
                    if y_coordinate >= 1:
                        grid[y_coordinate - 1][x_coordinate] += 1
                    if x >= 1:
                        grid[y_coordinate][x_coordinate - 1] += 1
        migrates = np.all(grid <= 3)

positions = [start_pos]


for i in range(steps):
    pos = positions[i]
    next_pos = sequence[i%len(sequence)] + pos
    if next_pos > 25:
        next_pos = next_pos -25
    positions.append(next_pos)
    x = pos//5
    y = pos%5 - 1
    if y == 0:
        x = x-1
    grid[y][x] += 1
    migrate()

migrate()
print(grid)