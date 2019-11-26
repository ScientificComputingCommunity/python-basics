#!/usr/bin/env python3

print('solving ax^2+bx+c=0 for real roots')

# define variables a, b & c
a = 1
b = 2
c = 1

delta = (b*b - 4.0*a*c)**0.5

x1 = -b + delta
x2 = -b - delta

x1 = x1/(2.0*a)
x2 = x2/(2.0*a)

print('Real roots', x1,x2)