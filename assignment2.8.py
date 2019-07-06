# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 05:43:07 2019

@author: Shri
"""

def generate_next_date(day,month,year):
    #Start writing your code here
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        if(day == 31):
            next_day = 1
            next_month = month+1
            next_year = year
        else:
            next_day=day+1
            next_month=month
            next_year=year
    
    if(month == 12):
        if(day == 31):
            next_day = 1
            next_month =1
            next_year = year+1
        else:
            next_day=day+1
            next_month=month
            next_year=year
    
    if(month == 2):
        if(day == 28):
            next_day = 1
            next_month = month+1
            next_year = year
        else:
            next_day=day+1
            next_month=month
            next_year=year
        
    if(month == 4 or month == 6 or month == 9 or month == 11):
        if(day == 30):
            next_day = 1
            next_month = month+1
            next_year = year
        else:
            next_day=day+1
            next_month=month
            next_year=year
    
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,12,2015)