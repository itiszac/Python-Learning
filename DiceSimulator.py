import random

while True:
    print('To roll dice enter \'roll\': ')
    if input().lower() == 'roll':
        print(random.randint(1, 7))
    else:
        break
