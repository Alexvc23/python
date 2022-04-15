from readline import append_history_file
import string
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

result=" " 
# game loop
while True:
    # The remaining amount of turns Thor can move. Do not remove this line.
    remaining_turns = int(input())
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if (initial_tx < light_x and initial_ty == light_y):
            result="E"
            initial_tx += 1
    if (initial_tx > light_x and initial_ty == light_y):
            result="W"
            initial_tx -= 1
    if (initial_tx == light_x and initial_ty > light_y):
            result="N"
            initial_ty -= 1
    if (initial_tx == light_x and initial_ty < light_y):
            result="S"
            initial_ty += 1
    if (initial_tx > light_x and initial_ty < light_y):
            result="SW"
            initial_tx -= 1
            initial_ty += 1
    if (initial_tx < light_x and initial_ty > light_y):
            result="NE"
            initial_tx -= 1
            initial_ty -= 1
    if (initial_tx > light_x and initial_ty > light_y):
            result="NW"
            initial_tx -= 1
            initial_ty -= 1
    if (initial_tx < light_x and initial_ty < light_y):
            result="SE"
            initial_tx += 1
            initial_ty += 1
    print(result)
            