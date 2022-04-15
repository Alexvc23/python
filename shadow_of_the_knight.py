
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
#batman position
x0, y0 = [int(i) for i in input().split()]
l, r, t, b = 0, w - 1, 0, h - 1

def formule(x0, y0):
    x0, y0 = ((l + r) / 2), ((t + b) / 2)
    return x0, y0


# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir == "DR":
        l, t =  x0 + 1, y0 + 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "DL":
        r, t = x0 - 1, y0 + 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "UR":
        l, b =  x0 + 1, y0 - 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "UL":
        r, b = x0 - 1, y0 - 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "D":
        r, l, t = x0, x0, y0 + 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "R":
        t, b, l = y0, y0, x0 + 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "U":
        r, l, b = x0, x0, y0 - 1
        x0 , y0 = formule(x0, y0)
    if bomb_dir == "L":
        t, b, r = y0, y0, x0 - 1
        x0 , y0 = formule(x0, y0)
    print(int(x0), int(y0), sep=" ")