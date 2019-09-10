from random import sample, shuffle
from colorama import Fore, Style
import os
import time

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
    
    side = 9
    row_nums = 1
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
    
    number = [range(1,10)]

    
    squares = side*side
    empties = squares * 1//dif_num
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
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

#defining square algorithm

#filling the empty grid
def fill_empty_grid(tbl,number):
    for e in range(81):
        row = e // 9
        column = e % 9
        if tbl[row][column] == 0:
            shuffle(number)
            for value in number:
                if not value in tbl[row]:
                    if not value in (tbl[0][column],tbl[1][column],tbl[2][column],tbl[3][column],tbl[4][column],tbl[5][column],tbl[6][column],tbl[7][column],tbl[8][column]):
                        sqr=[]
                        if row < 3:
                            if column < 3:
                                sqr = [tbl[i][0:3] for i in range(0,3)]
                            elif column < 6:
                                sqr = [tbl[i][3:6] for i in range(0,3)]
                            else:
                                sqr = [tbl[i][6:9] for i in range(0,3)]
                        elif row < 6:
                            if column < 3:
                                sqr = [tbl[i][0:3] for i in range(3,6)]
                            elif column < 6:
                                sqr = [tbl[i][3:6] for i in range(3,6)]
                            else:
                                sqr = [tbl[i][6:9] for i in range(3,6)]
                        else:
                            if column < 3:
                                sqr = [tbl[i][0:3] for i in range(6,9)]
                            elif column < 6:
                                sqr = [tbl[i][3:6] for i in range(6,9)]
                            else:
                                sqr = [tbl[i][6:9] for i in range(6,9)]
                        if not value in (sqr[0]+sqr[1]+sqr[2]):
                            tbl[row][column] = value
                            if check_full(board):
                                return True
                            else:
                                if fill_empty_grid(board,number):
                                    return True
            break
    tbl[row][column] = 0


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
def check_full(tbl):
    for row in range(0,9):
        for column in range(0,9):
            if tbl[row][column] == 0:
                return False

#Determine win condition
def win_lose (board, full_board):
    win = False
    board.sort()
    full_board.sort()
    if board == full_board:
        win = True
        print(Fore.GREEN + "Congratulations! You solved the puzzle!")
    else:
        print(Fore.RED + "You've got some of the numbers wrong, check them again!")
        print(Fore.GREEN + "Right board is: " "\n")
        print_sudoku(full_board)
    return win

#Showing the good solution if the sudoku has wrong numbers



main()