# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:29:45 2019

@author: Shri
"""

#Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
#Handle the possible errors in the code written inside the function.

#Sample Input	Expected Output
#16	120






def find_smallest_number(num):
    #start writing your code here
    a=0
    for i in range(1,(num**4)):
        factors = []
        for j in range(1,(i+1)):
            if(i%j == 0):
                factors.append(j)
        if(len(factors) == num):
             a=i
             break
    return a
        
     
        

num=79
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)