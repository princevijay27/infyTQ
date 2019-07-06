# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:46:17 2019

@author: Shri
"""

def calculate(distance,no_of_passengers):
             a = (distance/10)*70
             b=no_of_passengers*80
             c=b-a
             if(c>=0):
                 return c
             else:
                 return -1
                 
             
    



#Provide different values for distance, no_of_passenger and 7test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))