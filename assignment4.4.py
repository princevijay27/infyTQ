# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:31:44 2019

@author: Shri
"""

def check_palindrome(word):
        b=list(map(str,word))
        counter=0
        for i in range(len(b)):
            if(b[i] == b[((len(b)-1)-i)]):
                counter+=1
        print(counter)
        if(counter == len(b)):
            return True
        else:
            return False

status=check_palindrome("explode")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")