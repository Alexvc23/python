import sys
import math
from traceback import print_tb

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ─── INTPUT ─────────────────────────────────────────────────────────────────────
""" 
 5 5
 0 | * 
 """
# ─── OUTPUT ─────────────────────────────────────────────────────────────────────
""" 
0***0
|   |
|   |
|   |
0***0
 """

height, width = [int(i) for i in input().split()]
c, cv, ch = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(height):
    for j in range(width):
        if((i == 0 or i == (height -1)) and (j == 0 or j == (width - 1))):
            print(c, end='')
            continue
        if ((j == 0 or j == (width - 1)) and (i != 0 and i != (height - 1))):
            print(cv,end='')
            continue
        if ((j > 0 and j < width - 1) and (i == 0 or i == height - 1) ):
            print(ch, end='')            
        else: 
            print(' ', end='')
    print('\n', end='')