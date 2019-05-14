import random

with open('word list.txt') as f:
    word_list = f.readlines()

word = word_list[random.randint(0, 1000)]
temp_word = word
# print(word)

while len(temp_word) > 1:
    print('Guess a letter:')
    letter = input().lower()
    if letter in temp_word:
        print(f'{letter} is in the word {temp_word.count(letter)} times, you have '
              f'{len(temp_word) - temp_word.count(letter) - 1} letters left.')
        temp_word = temp_word.replace(letter, '')
    elif letter not in temp_word:
        print(f'{letter} is not in the word..')

if len(temp_word) <= 1:
    print(f'You won, the word was {word}')
