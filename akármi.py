from random import sample
import os
from colorama import Fore, Style

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







#rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ] 
#cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]            
#board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]