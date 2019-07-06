# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:29:47 2019

@author: Shri
"""

#Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list. If there are no duplicate values, it should return an empty list.

#Also write the pytest test cases to test the program.

#Sample Input	Expected Output
#[12,54,68,759,24,15,12,68,987,758,25,69]	[12, 68]


def find_duplicates(list_of_numbers):
    c={}
    for i in range(len(list_of_numbers)):
        for j in list_of_numbers[i+1: ]:
            if(list_of_numbers[i] == j):
                c[list_of_numbers[i]]=list_of_numbers[i]
    return list(c.keys())
    
                 
        
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)