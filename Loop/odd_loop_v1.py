#!/usr/bin/env python3
'''
Given an input N, print all odd numbers from 
1 to N
'''

print('Enter an integer value')
N = 10

print('Printing odd numbers between 1 and', N, '...')

for n in range(1,N):
    # check condition for being odd
    if n%2 == 0:
        pass
    else:
        print ('Found an odd number', n, '!')
    #if n%2 == 1:
    #    print ('Found an odd number', n, '!')
