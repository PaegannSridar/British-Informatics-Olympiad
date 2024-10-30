import itertools
import time

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

if __name__ == '__main__':
    ntgt = int(input())
    comb = 1
    nth = 0
    pwd = ''
    cont = True
    start = time.time()
    while cont:
        print(f"comb: {comb}, nth: {nth}")
        for c in itertools.combinations(characters, comb):
            pwd = ''.join(c)
            nth = nth + 1
            # print(f'{pwd}:{nth}')
            if nth == ntgt:
                cont = False
                break
        comb += 1
    print(f'password is: {pwd}')
    print(f'time taken: {time.time() - start}')