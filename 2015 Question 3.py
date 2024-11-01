import itertools
import more_itertools
import time

a,b,c,d,n = map(int,input().split())

start = time.time()
exhibition = a*'A' + b*'B' + c*'C' + d*'D'
nth = 0
pwd = ''
for c in more_itertools.distinct_permutations(exhibition, len(exhibition)):
    if nth == n-1:
        pwd = ''.join(c)
        cont = False
        break
    nth = nth + 1
end = time.time()
print(f'password is: {pwd}')
print('Time taken: ', end - start)
