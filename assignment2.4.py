# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:18:37 2019

@author: Shri
"""

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    name=current_currency_name
    amount=amount_needed_inr
    if(name == "Euro"):
        current_currency_amount=amount*0.01417
    elif(name == "British Pound"):
        current_currency_amount=amount*0.0100
    elif(name == "Australian Dollar"):
        current_currency_amount=amount*0.02140
    elif(name == "Canadian Dollar"):
        current_currency_amount=amount*0.02027
    elif(name != "Euro" and name != "British Pound" and name != "Australian Dollar" and name != "Canadian Dollar" ):
        current_currency_amount=-1
    return current_currency_amount
#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"china")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
    
    
    
    #Euro	0.01417
#British Pound	0.0100
#Australian Dollar	0.02140
#Canadian Dollar	0.02027
    