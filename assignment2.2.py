# -*- coding: utf-8 -*-
"""
Created on Wed May 29 00:30:23 2019

@author: Shri
"""

#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    sum=0
    diff=0
    for i in range(no_of_five):
        diff=rupees_to_make-sum
        if(sum <= rupees_to_make and diff>=5):
            sum=sum+5 
            
            five_needed+=1
            
        else:
             break
   # if(sum < rupees_to_make):
            
    for i in range(no_of_one):
        diff = rupees_to_make-sum
        if(sum < rupees_to_make and diff>=0 ):
             sum+=1 
             one_needed+=1
             
        else:
            break
                     
    if(sum == rupees_to_make):
        #return five_needed,one_needed
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)

        
    if(no_of_five >= five_needed and no_of_one == one_needed and sum < rupees_to_make):
        print(-1)
    
    
            

    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
#(no_of_five == five_needed and no_of_one == one_needed and sum < rupees_to_make)

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program

make_amount(93,19,2)
