#!/usr/bin/env python3
'''
Given an input N, print all odd numbers from 
1 to N
'''

print('Enter an integer value')
N = input()

# returned value from input has type string
# convert it to integer before we can use it
N = int(N)

print('Printing odd numbers between 1 and', N, '...')

for n in range(1,N):
    # check condition for being odd
    if n%2 == 1:
        print ('Found an odd number', n, '!')
