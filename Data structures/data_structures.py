#!/usr/bin/env python3

'''
This file introduces some data structures in Python 
and some of the methods associated with 
working with them
'''
# LISTS
# Declare lists
numbers = [1,2,3,4,5,6,7]

# access elements of a list
print('Printing numbers[0] outputs:',numbers[0])

# modify the content of the first index in numbers
# variable
numbers[0] = 10
print('Printing numbers[0] after modifying the content outputs:',numbers[0])

# we can generate lists with the range function
numbers = list(range(1,8))
print('Printing the output of numbers generated with range',numbers)

# we can have lists that are strings
names = ['Kwasi', 'Esi', 'Kojo', 'Adjoa', 'Kwabena', 'Abena']
# print them all out
for name in names:
    print(name)

# you can show part of a list
# this is called slicing
# we can do that by
print (names[0:2])
# or 
print (names[0:])
# or
print (names[:4])

# list methods
# append
# list.append(x)
my_list = ['a', 'b', 'c']
my_list.append('d')

print ('my modified list:',my_list)
# find some more methods here:
# https://docs.python.org/3/tutorial/datastructures.html

# Example
squares = []
for i in range(10):
    squares.append(i**2)
print ('my list of squares:', squares)

# Exercise 
# 1. Open a new file. Inside this file, create a list.
# 2. Assign some elements to this list and print them out in a loop
# 3. Save the file and run it

# TUPLES
# declare tuple
my_tuple = 12,8,24,7,9,'A'
print ('Printing contents of my_tuple:',my_tuple)

# try assigning a value ...

# SETS
# unordered, does not allow duplicates
word = 'Kkaallallaaq'
print(set(word))

# supports: 
alpha = {'a', 'b', 'c', 'd', 'e'}
beta = {'b', 'c', 'a', 'f', 'z'}

# union |   (in a or b or both)
print ('finding union (alpha | beta) :',alpha | beta)

# intersection &   (in a and b)
print ('finding intersection (alpha & beta) :',alpha & beta)

# difference -   (in a but not in b)
print ('finding difference (alpha - beta) :',alpha - beta)

# disjunctive union ^  (in a or b but not in both)
print ('finding disjunctive union (alpha ^ beta) :',alpha ^ beta)


# DICTIONARIES
# declare a dictionary
# key: value pairs
my_dictionary = {}

telephone_numbers = {'Kofi': '+233200000000', 'Ama': '+233240000000'}
print ("Kofi's number:",telephone_numbers['Kofi'])
