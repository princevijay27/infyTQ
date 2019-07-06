# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:53:19 2019

@author: Shri
"""

def is_palindrome(word):
    b=word.lower()
    value=0
    for i in range(len(word)):
        if(b[i] == b[len(word)-i-1]):
            value+=1
    if(value == len(word)):
        return True
    else:
        return False
    

#Provide different values for word and test your program
result=is_palindrome("malaYALAM")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")