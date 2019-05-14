import random

print('Guess a number between 1-100:')
number = random.randint(1, 101)
# print(number)

while True:
    guess = int(input())
    if number == guess:
        print('You\'re correct')
        break
    elif number > guess:
        print('higher')
        continue
    else:
        print('lower')
        continue

