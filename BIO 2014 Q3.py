characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
              '4', '5', '6', '7', '8', '9']

#n = int(input("Enter the value of n: "))
counter = 0

def function1(fixed_character):
    for i in range(0, 38):
        password = characters[0:fixed_character] + list(characters[i])
        print(password)


function1(3)

