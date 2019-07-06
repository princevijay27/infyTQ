# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:51:21 2019

@author: Shri
"""

def find_new_salary(current_salary,job_level):
    level=job_level
    income=current_salary
    increment=0
    new_salary=0
    if(level == 5):
        increment=int(income*(5/100))
        new_salary=income+increment
    elif(level == 4):
        increment=int(income*(7/100))
        new_salary=income+increment
    elif(level == 3):
        increment=int(income*(15/100))
        new_salary=income+increment
    elif(level!=3 and level!=4 and level!=5):
        increment=int(income*(0/100))
        new_salary=income+increment
        
    
    
    
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(13456,0)
print(new_salary)