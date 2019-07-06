# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:01:17 2019

@author: Shri
"""

def check_double(number):
    double_number=number*2
    a=list(map(int,str(number)))
    b=list(map(int,str(double_number)))
    v=0
    c=0
    for i in a:
        for j in b:
            if(i == j):
               v+=1
    for i in range(len(a)):
        if(a[i] != b[i]):
            c+=1
    if(v == len(a) and c == len(a)):
        return True
    else:
        return False
        
    
    
    
    
    
    
print(check_double(125874))
251748