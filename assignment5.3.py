# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 01:33:46 2019

@author: Shri
"""

def create_largest_number(number_list):
    number_list.sort(reverse=True)
    res = int("".join(map(str, number_list))) 
    return res 
  

    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)