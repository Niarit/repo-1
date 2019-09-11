from random import sample
from colorama import Fore, Style
import os
import time
import copy

def main():
    
    difficulty = input(Fore.BLUE + "Choose difficulty (easy, medium, hard, extreme): ")
    print(Fore.WHITE)
    if difficulty == "easy":
        dif_num = 32
    elif difficulty == "medium":
        dif_num = 16
    elif difficulty == "hard":
        dif_num = 8
    else:
        dif_num = 4

    board = fill_grid()
    full_board = copy.deepcopy(board)
    
    squares = 9*9
    empties = squares * 1//dif_num
    for p in sample(range(squares),empties):
        board[p//9][p%9] = 0
    numSize = 1
    print_sudoku(board)
    
    while True:
        try:
            row = int(input("Enter the number of the row: "))
            column = int(input("Enter the number of the column: "))
            num = int(input("Enter your number: "))
        except ValueError:
            print("Invalid input")
            continue
        if board[row-1][column-1] == 0:
            board[row-1][column-1] = num
        else:
            print("You can't touch this!")
            time.sleep(3)
        print_sudoku(board)
        if check_full(board) == True:
            user_ans = input("Would you like to check your board? (y/n): ")
            if "y" in user_ans:
                win_lose(board,full_board)
            else:
                print_sudoku(board)
                continue
            break
        continue
        
#Formating
def print_sudoku(tbl):
    os.system('clear')
    print (f"{0}| {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |")
    print("-"*38)
    for i, row in enumerate(tbl):
        print(("{}".format(i+1)) + ("|" + " {}   {}   {} |"*3).format(*[x if x != 0  else Fore.MAGENTA + "#" + Fore.WHITE  for x in row]))
        if i == 8:
            print("-"*38)
        elif i % 3 == 2:
            print(" " "|" + "---+"*8 + "---|")
        else:
            print(" " "|" + "   +"*8 + "   |")

# Cheking for remaning holes in the table
def check_full(board):
    full = True
    for row in board:
        for element in row:
            if element == 0:
                full = False
    return full

#Determine win condition
def win_lose (board, full_board):
    win = False
    if full_board == board:
        win = True
        print(Fore.GREEN + "Congratulations! You solved the puzzle!")
    else:
    #Showing the good solution if the sudoku has wrong numbers
        print(Fore.RED + "You've got some of the numbers wrong, check them again!")
        print(Fore.GREEN + "Right board is: " "\n")
        time.sleep(2)
        print_sudoku(full_board)
    return win


def fill_grid():
    board = []
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    board.append([0,0,0,0,0,0,0,0,0,0])
    rows = []
    cols = []

    base  = 3 
    side  = base*base
    nums  = sample(range(1,side+1),side) # random numbers

    for g in sample(range(base), base):
        for r in sample(range(g*base,(g+1)*base), base):
            rows.append(r)

    for g in sample(range(base), base):
        for c in sample(range(g*base,(g+1)*base), base):
            cols.append(c)

    for r in range(side):
        for c in range(side):
            board[r][c] = nums[(base * (r % base) + r // base + c) % side]

    board = [[board[r][c] for c in cols] for r in rows]
    for line in board: print(line)
    return board


main()
