import random
import os
from colorama import Fore, Style

side = 9
row_nums = 1
board = []
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0])

numberList=[1,2,3,4,5,6,7,8,9]

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def fillGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      random.shuffle(numberList)      
      for value in numberList:
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if check_full(board):
                return True
              else:
                if fillGrid(board):
                  return True
  
            
# Cheking for remaning holes in the table
def check_full(tbl):
    for row in range(0,9):
        for column in range(0,9):
            if tbl[row][column] == 0:
                return False

fillGrid(board)
print(board)
