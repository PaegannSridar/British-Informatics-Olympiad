import time

#num = int(input("Enter a number: "))

start = time.time()

oddNumbers = list(range(1, 200000))[::2]

luckyNumbers = oddNumbers[:]

for i in oddNumbers[1:]:
    if i in luckyNumbers:
        to_remove = []
        for idx, _ in enumerate(luckyNumbers):
            if (idx+1) % i == 0:
                to_remove.append(luckyNumbers[idx])
        for number in to_remove:
            if number in luckyNumbers:
                luckyNumbers.remove(number)
print(luckyNumbers)
print(len(luckyNumbers))

"""results = []
for num in range(2, luckyNumbers[100]):
    for i in luckyNumbers:
        if i > num:
            #print(luckyNumbers[luckyNumbers.index(i)-1], i)
            results.append((luckyNumbers[luckyNumbers.index(i)-1], i))
            break
results = set(results)
print(len(results))"""

end = time.time()
print(end - start)
