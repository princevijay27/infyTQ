# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:53:47 2019

@author: Shri
"""

def find_product(num1,num2,num3):
    product=0
    if(num1 == 7):
        product=num2*num3
    elif(num2 == 7 ):
        product=num3
    elif(num3 == 7):
        product=-1
    elif(num1!=7,num2!=7,num3!=7):
        product=num1*num2*num3
    return product
   

product=find_product(4,3,2)
print(product)