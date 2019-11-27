#!/usr/bin/env python3
'''
Given an input N, print all odd numbers from 
1 to N
'''
# define your function
def is_odd(number):
    '''
    Return True if number is odd
    or False otherwise
    '''
    if number%2 == 1:
        return True
    else:
        return False

print('Enter an integer value')
N = input()

# returned value from input has type string
# convert it to integer before we can use it
N = int(N)

print('Printing odd numbers between 1 and', N, '...')

for n in range(1,N):
    # check condition for being odd
    if is_odd(n):
        print ('Found an odd number', n, '!')
