from string import ascii_uppercase
from random import choice

alphabet = ascii_uppercase
alphabet_display = [i for i in alphabet]
row = 0
reset = '\033[0m'
grey = '\033[1;30m'
green = '\u001b[32m'
yellow = '\u001b[33m'
purple = '\033[0;35m'

def show_board():
    print('\n')
    for row in board: 
        print(*row)
    print('\n\n',*alphabet_display,'\n')

def set_color_and_upper(text, color):
    return f'{color}{text.upper()}{reset}'

def loadWords():
    inFile = open('word-list.txt', 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList

board = [['_' for j in range(5)] for i in range(6)]
word_list = loadWords()
answer = choice(word_list)

show_board()

while row < 6:
    guess = input("Enter a 5-letter word: ")

    if len(guess) != 5:
        print("Word must be exactly 5 letters, please enter a new word")
        continue

    if not guess in word_list:
        print('Invalid word, try again')
        continue

    correct_count = 0
    temp_answer = list(answer)
    for index, letter in enumerate(guess):
        if temp_answer.count(letter) > 0:
            temp_answer.remove(letter)
            if letter == answer[index]:
                new_letter = set_color_and_upper(letter, green)
                correct_count += 1
            else:
                new_letter = set_color_and_upper(letter, yellow)
        else:
            new_letter = set_color_and_upper(letter, grey)
        
        board[row][index] = new_letter
        alphabet_display[alphabet.index(letter.upper())] = new_letter
    
    show_board()
    
    if correct_count == 5:
        print(f'You win! Tries: {row + 1}')
        break

    if row == 5:
        print(f'Game over. The word was {set_color_and_upper(answer, purple)}.')
        break

    row += 1