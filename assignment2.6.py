# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:50:54 2019

@author: Shri
"""

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    type=food_type
    distance=distance_in_kms
    quantity=quantity_ordered
    if(type=="V" and distance > 0 and quantity >=1):
        if(distance <=3 ):
            bill_amount = 120*quantity + 0
        if(distance >3 and distance <= 6 ):
            bill_amount = 120*quantity + 3*distance
        if(distance > 6 ):
            bill_amount = 120*quantity + 6*distance
    elif(type=="N" and distance > 0 and quantity >=1):
        if(distance <=3 ):
            bill_amount = 150*quantity + 0
        if(distance >3 and distance <= 6 ):
            bill_amount = 150*quantity + 3*(distance-3)
        if(distance > 6 ):
            bill_amount = 150*quantity + 6*(distance-6)
    else:
        bill_amount=-1
            
       
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)


#For first 3kms	0
#For next 3kms	3
#For the remaining	6