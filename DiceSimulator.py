import random

while True:
    print('To roll die enter \'roll\' or \'exit\' to quit game: ')
    decision = input().lower()
    if decision == 'roll':
        print(random.randint(1, 7))
    elif decision == 'exit':
        print('Goodbye!')
        break
    else:
        continue
