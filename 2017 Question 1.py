colours = ['R', 'G', 'B']
first_row = list(input())
current_row = first_row.copy()
next_row = []

for i in range(len(first_row) - 1):
    for j, next_j in zip(current_row, current_row[1:]):
        if j == next_j:
            next_row.append(j)
        else:
            remaining_colour = (set(colours) - {j, next_j}).pop()
            next_row.append(remaining_colour)
    current_row = next_row
    next_row = []

print(current_row.pop())