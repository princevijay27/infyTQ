#-*- coding: utf-8 -*-
"""
Created on Thu May 23 10:19:17 2019

@author: Shri
"""

def find_leap_years(given_year):
    #given_year+=1
    list_of_leap_years=[]
    counter=0
    for i in range(70):
            if(given_year%4 == 0 and given_year%100 != 0):
                x=given_year
                list_of_leap_years.append(x)
                given_year+=1
                counter+=1
            elif(given_year%400 == 0):
                x=given_year
                list_of_leap_years.append(x)
                given_year+=1
                counter+=1
            elif(counter == 15):
                 break
            else:
                given_year+=1
        
    return list_of_leap_years

list_of_leap_years=find_leap_years(1684)
print(list_of_leap_years)