import sys
import math
import pdb
from pudb import set_trace; 

# Don't let the machines win. You are humanity's last hope...

pdb.set_trace()
set_trace()
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
l = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    l.append(line)
    
r = ""
i = 0
j = 0
n = 0
b = 0

def find_next(str, start):
    i = start
    while (i < len(str)):
        if (str[i] == '0'):
            return(i)
        i += 1
    return (0)

def find_below(list, ind_list, ind_str):
    for i in range(ind_list, len(list)):
        try:
            if (list[i][ind_str] == '0'):
                return (i)
        except IndexError:
            return (0)
    return (0)

while ( i < len(l)):
    j = 0
    while (j < len(l[i])):
        n = find_next(l[i], j+1)
        b = find_below(l,i+1, j)
        if ((l[i][j] == '0' and n != 0)):
            r += str(j)+' '+str(i) +' '+str(n)+' '+str(i) + ' '
        else:
            r += str(j)+' '+str(i) +" -1 -1 "
        if ((l[i][j] == '0' and b != 0)):
            r += str(j) + ' ' + str(b)
        else:
            r += "-1 -1"
        print(r)
        r = ""
        j = n if n else (j + 1)
    i += 1


    


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
