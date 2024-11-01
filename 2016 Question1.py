def calculate_promenade_value(promenade):
    l, m = 1, 0
    r, s = 0, 1

    for choice in promenade:
        if choice == 'L':
            l, m = l + r, m + s
        elif choice == 'R':
            r, s = r + l, s + m

        result = [l+r, m+s]
    return result


promenade_input = input("Enter the promenade sequence: ").strip().upper()
result_fraction = calculate_promenade_value(promenade_input)

print(f"{result_fraction[0]} / {result_fraction[1]}")
