import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

""" Pigeonhole
There is a cage of  pigeons in the terrace,  the cage 
has h number of holes,  and p number of pigeons, they 
want to have a party inside the cage, but to do so, they 
have to get inside cage one by one from hole 0 to h. If 
there are fewer pigeons than holes, then there will be at 
least one hole empty. For instance, if I have 3 pigeons and 
4 holes, there will be 1 pigeon per hole and one hole empty. 
If I have more pigeons than holes, they will have  to  get 
inside the cage one by one up to the last hole and restart 
from the first one up until all the pigeons have got inside. 
For instance, if I have 4 pigeons and 3 holes, There will be 
1 pigeon by hole and the last one will enter to the first. 
Being the first hole, the one with more pigeons. 2 1 1. """

h = int(input())
p = int(input())

c = [0] * h
for i in range(p):
    c[i%h] += 1
index = len(c) - 1
_max = max(c)
for j in reversed(c):
    if j == _max:
        break
    index -= 1
print(c)
print(index, _max, sep='\n')