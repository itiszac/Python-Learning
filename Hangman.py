import random

with open('word list.txt') as f:
    word_list = f.readlines()

word = word_list[random.randint(0, 1000)]
guess_word = ''
print(word)

while guess_word != word:
    print('Guess a letter:')
    letter = input().lower()
    if letter in word:
        print(f'{letter} is in the word {word.count(letter)} times')
    elif letter not in word:
        print(f'{letter} is not in the word..')

# print(word)
