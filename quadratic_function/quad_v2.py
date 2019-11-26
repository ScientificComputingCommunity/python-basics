#!/usr/bin/env python3

print('solving ax^2+bx+c=0 for real roots')

# define variables a, b & c
a = 1
b = 4
c = 4

delta = b*b - 4.0*a*c
# check condition for what would make the 
# roots real or not
if delta < 0.0:
    print('No real roots')
else:
    delta = delta**0.5
    x1 = -b + delta
    x2 = -b - delta

    x1 = x1/(2.0*a)
    x2 = x2/(2.0*a)
    print('Real roots', x1,x2)
