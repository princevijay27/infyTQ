# -*- coding: utf-8 -*-
"""
Created on Fri May 24 00:30:26 2019

@author: Shri
"""
def perfect_number(number):
    l=[]
    sum=0
    for i in range(1,1000):
        if(number%i == 0):
            if(i!=number):
              l.append(i)
    for i in l:
        sum=sum+i
    print(sum)
    print(l)
    if(sum == number):
            print("this is perfect no.")
    else:
           print("this is not perfect no.")
    

num=int(input("enter the number"))
perfect_number(num)
        
        
        
