# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 05:01:34 2019

@author: Shri
"""

def encode(message):

    q=list(map(str,message))
    q.append("0")
    print(q)
    counter=0
    v=[]
    p=1
    for i in range(1,len(q)):
        if(q[counter] == q[i]):
           counter+=1
           p+=1
        else:
           v.append(str(p)+q[counter])
           p=1
           counter+=1

    sum=""
    for i in v:
        sum=sum+i
    return str(sum)
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("M")
print(encoded_message)


#q=list(map(str,message))
#counter=0
#v=[]
#p=1
#for i in range(1,len(q)):
 #       if(q[counter] == q[i]):
#           counter+=1
#           p+=1
#        if(i != len(q) and q[counter] != q[i]):
#            v.append(str(p)+q[counter])
#            p=1
#            counter+=1
#        if(i == (len(q)-1)):
#           v.append(str(p)+q[counter])
#if(len(q) == 1):
#    v.append(str(len(q))+q[(len(q)-1)])
           
#sum=""
#for i in v:
#        sum=sum+i
#return str(sum)