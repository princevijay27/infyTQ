# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 03:32:31 2019

@author: Shri
"""
def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    

    #Start writing your code here
   # print(len(str(account_number)))
    #print(str(account_number)[0])
    
            
    if(len(str(account_number)) == 4  and  str(account_number)[0] == "1"):
        #print("Account number:", account_number)
        if(account_balance >= 100000):
          
            if(loan_type == "Car"):
               if(salary > 25000):
                eligible_loan_amount=500000	
                bank_emi_expected=36
                if(eligible_loan_amount >= loan_amount_expected and bank_emi_expected >= customer_emi_expected):
                               print("Account number:", account_number)
                               print("The customer can avail the amount of Rs.", eligible_loan_amount)
                               print("Eligible EMIs :", bank_emi_expected)
                               print("Requested loan amount:", loan_amount_expected)
                               print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
                    
                
               else:
                  print("Invalid loan type or salary")
           
          
            if(loan_type == "Business"):
              if(salary > 75000):
                eligible_loan_amount=7500000		
                bank_emi_expected=84
                if(eligible_loan_amount >= loan_amount_expected and bank_emi_expected >= customer_emi_expected):
                               print("Account number:", account_number)
                               print("The customer can avail the amount of Rs.", eligible_loan_amount)
                               print("Eligible EMIs :", bank_emi_expected)
                               print("Requested loan amount:", loan_amount_expected)
                               print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
                    
                
              else:
                print("Invalid loan type or salary") 
            
            
            if(loan_type == "House"):
              if(salary > 50000):
                eligible_loan_amount=6000000		
                bank_emi_expected=60
                if(eligible_loan_amount >= loan_amount_expected and bank_emi_expected >= customer_emi_expected):
                               print("Account number:", account_number)
                               print("The customer can avail the amount of Rs.", eligible_loan_amount)
                               print("Eligible EMIs :", bank_emi_expected)
                               print("Requested loan amount:", loan_amount_expected)
                               print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
                    
              else:
                print("Invalid loan type or salary")
            
            
            if(loan_type!="Car" and loan_type!="Business" and loan_type!="House"):
                 print("Invalid loan type or salary") 
                
            
               
        
        else:
            print("Insufficient account balance")
        
            
            
    else:
        print("Invalid account number")
    
        
            
        
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
#> 25000	Car	500000	36
#> 50000	House	6000000	60
#> 75000	Business	7500000	84