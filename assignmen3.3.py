# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 02:11:06 2019

@author: Shri
"""
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if(num1+num2>num3  and  num2+num3>num1 and num1+num3>num2):
        return success
    else: 
        return failure


    #Write your logic here

    #Use the following messages to return the result wherever necessary
   

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
p=form_triangle(num1, num2, num3)
print(p)