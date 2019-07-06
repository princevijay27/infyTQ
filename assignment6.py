# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:27:22 2019

@author: Shri
"""


def is_palindrome(st):
    n = len(st) 
    st = st.upper()
     
    if (n == 0) : 
        return True
      
    return isPalRec(st, 0, n - 1);

def isPalRec(st, s, e) : 
      
    
    if (s == e): 
        return True
  
   
    if (st[s] != st[e]) : 
        return False 
    if (s < e + 1) : 
        return isPalRec(st, s + 1, e - 1); 
  
    return True


result=is_palindrome("MaddAm")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")