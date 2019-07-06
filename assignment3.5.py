# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:38:25 2019

@author: Shri
"""

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    a=0
    if(legs%2==0):
        if(legs%4==0):
            a=legs/2
            chicken_count=a/2
            b=a/4
            print(b)
            print(type(b))
            if(type(b) == int):
               rabbit_count=b
            print(chicken_count,rabbit_count)
        #elif():
                
    

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(150,400)



#Sample Input	    Expected Output
#heads-150 legs-400	  100 50
#heads-3 legs-11	  No solution
#heads-3 legs-12	  0 3
#heads-5 legs-10	  5 0