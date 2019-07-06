# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 01:13:54 2019

@author: Shri
"""

def find_max(num1, num2):
    max_num=-1
    b=[]
    if(num1<num2):
        for i in range(num1,num2+1):
            a=int(i/10)
            c=i%10
            sum=a+c
            if(sum%3 == 0):
                count=0
                for j in str(i):
                    count+=1
                if(count == 2):
                    if(i%5 == 0):
                        b.append(i)
                    else:
                        max_num=-1
                else:
                    max_num=-1
            else:
                 max_num=-1
        
        
        for i in range(len(b)):
            for j in range(1+i,len(b)):
                 print(j)
                 if(b[i]<b[j]):
                   b[i],b[j] = b[j],b[i]
        if(len(b) == 0):
            max_num=-1
        else:
           max_num=b[0]
    else:
        max_num=-1
             
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(24,34)
print(max_num)
#Sum of the digits of the number is a multiple of 3
#Number has only two digits
#Number is a multiple of 5


#method how to divide two number
#a,b=0,0
#num=34
#a=int(num/10)   
#b=num%10
#print(a,b)

#for i in range(10,20):
#    b=list(map(int,str(i)))
#    sum=0
  #  for j in str(i):
 #   for j in b:
 #       print(j)
 #       sum=sum+j
#        print(sum)