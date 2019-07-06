# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 03:10:49 2019

@author: Shri
"""

#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    m=0
    if(set(reqd_gems) <= set(gems_list)):
        for i,j in zip(reqd_gems,reqd_quantity):    
            counter=0
            for k in gems_list:
                 counter+=1
                 if(k == i):
                     b=0
                     b=j*price_list[counter-1]
                     bill_amount=bill_amount+b
    else:
        bill_amount=-1
        
    if(bill_amount > 30000):
        m=bill_amount*(5/100)
        bill_amount=bill_amount-m
            
                
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)