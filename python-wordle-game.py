from random import choice

board = [["_","_","_","_","_"] for i in range(6)]
row = 0
reset = '\033[0m'
grey = '\033[1;30m'
green = '\033[1;32m'
yellow = '\033[1;33m'
purple = "\033[0;35m"

def space_out(x):
    return ' '.join(x)

def show_board():
    for row in board:
        print(space_out(row))

def set_color(text, color):
    return f'{color}{text}{reset}'

def loadWords():
    # print("Loading word list from file...")
    inFile = open('word-list.txt', 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    # print("  ", len(wordList), "words loaded.")
    return wordList

# words = ['puree', 'grape', 'fishy', 'start', 'large', 'small', 'extra', 'tacos', 'plump', 'wiley', 'paled', 'story']
word_list = loadWords()
answer = choice(word_list)
        
show_board()

while row < 6:
    guess = input("Enter a 5-letter word: ")

    if len(guess) != 5:
        print("Word must be exactly 5 letters, please enter a new word")
        continue

    # check if entered word is a valid word

    correct_count = 0
    temp_answer = list(answer)
    for index, letter in enumerate(guess):
        if letter == answer[index]:
            board[row][index] = set_color(letter.upper(), green)
            temp_answer.remove(letter)
            correct_count += 1
        elif temp_answer.count(letter) > 0:
            board[row][index] = set_color(letter.upper(), yellow)
            temp_answer.remove(letter)
        else:
            board[row][index] = set_color(letter.upper(), grey)
    
    show_board()
    
    if correct_count == 5:
        print(f'You win! Tries: {row + 1}')
        break

    if row == 5:
        print(f'Game over. The word was {set_color(answer.upper(), purple)}.')
        break

    row += 1
