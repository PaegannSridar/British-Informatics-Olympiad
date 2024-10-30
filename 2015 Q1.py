def get_adjacent_partitions(lst):
    n = len(lst)
    partitions = []

    for start in range(n):
        for end in range(start + 1, n+1):
            current_group = lst[start:end]

            if end == n:
                partitions.append([current_group])
            else:
                remaining = lst[end:]
                next_partitions = get_adjacent_partitions(remaining)

                for next_partition in next_partitions:
                    partitions.append([current_group] + next_partition)

    return partitions

my_list = list('BBIIOIIBB')
partitions = get_adjacent_partitions(my_list)

valid_partitions = []
for partition in partitions:
    all_elements = []
    for item in partition:
        for i in item:
            all_elements.append(i)
    if all_elements == my_list:
        valid_partitions.append(partition)

valid_partitions2 = []
for partition in valid_partitions:
    if partition == partition[::-1] and len(partition) > 1:
        valid_partitions2.append(partition)

for valid_partition in valid_partitions2:
    print(valid_partition)

print(len(valid_partitions2))