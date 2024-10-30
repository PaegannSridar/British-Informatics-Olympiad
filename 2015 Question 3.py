import itertools
from itertools import combinations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())

exhibition = a*'A' + b*'B' + c*'C' + d*'D'


count = 0

combinations = sorted(set(list(itertools.permutations(exhibition, len(exhibition)))))
for i in combinations:
    if count == n-1:
        print(i)
        break
    count += 1