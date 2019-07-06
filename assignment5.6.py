# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:36:36 2019

@author: Shri
"""

     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    for i in item_tuple:
        v=0
        if(type(i) == str):
            for j in menu:
                if(i == j):
                    v+=1
                    print(i+" " +"is available")
            if(v != 1):
                print(i + " "+ "is not available")
    for i in range(len(item_tuple)):
        b=0
        if(type(item_tuple[i]) == str):
          for k,j in zip(menu,quantity_available):
            b+=1
            if(item_tuple[i] == k):
                a=check_quantity_available((b-1),item_tuple[i+1])
                quantity_available[b-1]=quantity_available[b-1]-item_tuple[i+1]
                if(a != True):
                       print(item_tuple[i] + " " + "stock is over")
          
          

    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index] >= quantity_requested):
        return True
    else:
        return False

#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)


#menu=['Veg Roll','Noodles','Fried Rice','Soup']
#a=("Veg Roll",2,"Noodles",2)
#for i in a:
#   if(type(i) == str): 
#    if(i in menu):
#        print(i)
#    else:
#        print("no")