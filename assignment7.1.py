# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:32:58 2019

@author: Shri
"""

#Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 
#Also write the pytest test cases to test the program.


#Sample Input	Expected Output
#12300	12321
#12331	12421
import functools
def nearest_palindrome(number):
     n=list(map(str,str(number)))
     c=len(n)
     s,v=0,0
     q=0
#case1 when number is palindrom and this will also cover the ("9999" next palindrom number)
     for s in range(len(n)//2):
         if(n[s] == n[len(n)-s-1]):
             v+=1
         if(v == (len(n)//2)): 
             q="p"
             if(len(n)%2==0):
                  
                  p=0
                  for i in range(c):
                     if(int(n[i]) == 9):  
                         p+=1
                  if(p == c):
                     v=functools.reduce(lambda z,y:z+y , n)
                     v=str(int(v)+2)
                     n=list(map(str,v))
                  else:     
                       n[(c//2)]=str(int(n[(c//2)])+1)
                       n[(c//2)-1]=str(int(n[(c//2)-1])+1)
             else:
              p=0
              for i in range(c):
                  if(int(n[i]) == 9):
                         p+=1
              if(p == c):
                 v=functools.reduce(lambda z,y:z+y , n)
                 v=str(int(v)+2)
                 n=list(map(str,v))
              else:    
                 n[(c//2)]=str(int(n[(c//2)])+1)
#case2 when the number is not palindromic and length of the number                  
     if(c%2==0 and q != "p"):
        if(c>=2):
         if(n[(c//2)-1] > n[(c//2)]):
             for i in range(c//2):
                 n[c//2+i]=n[(c//2)-1-i]
                 
         elif(n[(c//2)-1] < n[(c//2)]):
             n[(c//2)-1]=str(int(n[(c//2)-1])+1)
             for i in range(c//2):
                 n[c//2+i]=n[(c//2)-1-i]
                 
         elif(n[(c//2)-1] == n[(c//2)]):
             
            if(c>2):
              if(n[(c//2)-1-1] < n[(c//2)+1]):
                 n[(c//2)-1]=str(int(n[(c//2)-1])+1)
                 for i in range(c//2):
                     n[c//2+i]=n[(c//2)-1-i]
                     
              elif(n[(c//2)-1-1] > n[(c//2)+1]):
                  for i in range(c//2):
                     n[c//2+i]=n[(c//2)-1-i]
                     
              elif(n[(c//2)-1-1] == n[(c//2)+1]):
                 for i in range(c//2):
                  f=0
                  if(n[((c//2)-1)-i] == n[((c//2)-1)+i]):
                      f+=1
                  else:
                      if(n[((c//2)-1)-i]>n[((c//2)-1)+i]):
                          for i in range(c//2):
                              n[c//2+i]=n[(c//2)-1-i]
                      elif(n[((c//2)-1)-i]>n[((c//2)-1)+i]):
                          n[(c//2)-1]=str(int(n[(c//2)-1])+1)
                          for i in range(c//2):
                               n[c//2+i]=n[(c//2)-1-i]
#case3 when the length of the number is odd and number is ont palindromic
     elif(c%2 != 0 and q != "p"):
        if(c>=3): 
         d=(c//2)
         
         if(n[d-1]>n[d+1]):
             if(int(n[d]) !=9):
                 for i in range(d):
                    n[d+i+1]=n[d-1-i]
             elif(int(n[d]) == 9 ):
                 n[d]=str(0)
                 n[d-1]=str(int(n[d-1])+1)
                 for i in range(d):
                    n[d+i+1]=n[d-1-i]          
                 
         elif(n[d-1]<n[d+1]):
             
             if(int(n[d]) !=9):
                n[d]=str(int(n[d])+1)
                for i in range(d):
                    n[d+i+1]=n[d-1-i]
                    
             elif(int(n[d]) == 9 ):
                 n[d]=str(0)
                 n[d-1]=str(int(n[d-1])+1)
                 for i in range(d):
                    n[d+i+1]=n[d-1-i]
                 
                    
         elif(n[d-1] == n[d+1]):
              for i in range(d):
                  f=0
                  if(n[d-i-1] == n[d+i+1]):
                      f+=1
                  else:
                      if(n[d-i-1]>n[d+i+1]):
                          for i in range(d):
                              n[d+i+1]=n[d-1-i]
                      elif(n[d-i-1]<n[d+i+1]):
                          n[d]=str(int(n[d])+1)
                          for i in range(d):
                               n[d+i+1]=n[d-1-i]             
#case4 when the length of the number is a single digit          
        elif(c == 1):
            if(int(n[0]) != 9):
               n=str(int(n[0])+1)
            else:
                n=str(int(n[0])+2)
            
     return int(functools.reduce(lambda z,y:z+y , n))      
    #start writitng your code here

number=11

print(nearest_palindrome(number))

