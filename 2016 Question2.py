import numpy as np

start_pos, sequence_length, steps = map(int, input().split())
sequence = input().split()
sequence = [int(i) for i in sequence]

grid = np.zeros((11, 11), dtype=int)

def migrate():
    global grid
    migrate = np.any(grid >= 4)
    while migrate:
        positions = np.where(grid >= 4)
        positions_list = list(zip(positions[0], positions[1]))
        for position in positions_list:
            grid[position[0], position[1]] -= 4
            grid[position[0], position[1] + 1] += 1
            grid[position[0] + 1, position[1]] += 1
            grid[position[0], position[1] - 1] += 1
            grid[position[0] - 1, position[1]] += 1
        migrate = np.any(grid >= 4)

for i in range(steps):
    if i == 0:
        pos = start_pos
    y = (pos-1)//5
    x = (pos-1)%5
    grid[y+3][x+3] += 1
    migrate()

    pos = sequence[i%len(sequence)] + pos
    if pos > 25:
        pos = pos%25

# migrate()
print(grid[3:8, 3:8])