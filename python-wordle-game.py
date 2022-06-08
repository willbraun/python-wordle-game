from random import choice

words = ['puree', 'grape', 'fishy', 'start', 'large', 'small', 'extra', 'tacos', 'plump', 'wiley', 'paled', 'story']
answer = choice(words)
board = [["_","_","_","_","_"] for i in range(6)]
row = 0
reset = '\033[0m'
grey = '\033[1;30m'
green = '\033[1;32m'
yellow = '\033[1;33m'

def space_out(x):
    return ' '.join(x)

def show_board():
    for row in board:
        print(space_out(row))

def set_color(text, color):
    return f'{color}{text}{reset}'
        
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
            board[row][index] = set_color(letter, green)
            temp_answer.remove(letter)
            correct_count += 1
        elif temp_answer.count(letter) > 0:
            board[row][index] = set_color(letter, yellow)
            temp_answer.remove(letter)
        else:
            board[row][index] = set_color(letter, grey)
    
    if correct_count == 5:
        print(f'You win! Tries: {row + 1}')
        break

    show_board()
    row += 1

print(f'Game over. The word was {answer}')