# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:12:55 2019

@author: Shri
"""

def find_pairs_of_numbers(num_list,n):
    subset=0
    a=0
    for i in range(len(num_list)):
        for j in  range(i,len(num_list)):
            
            if(num_list[i] == num_list[j] and i == j):
                a=a+1
              #  print(num_list[i])
               # print(num_list[j])
            elif(n == (num_list[i]+num_list[j])):
                #print(num_list[i])
                #print(num_list[j])
                subset+=1
    return subset
    #Remove pass and write your logic here

num_list=[1, 2, 4, 6, 5]
n=6
print(find_pairs_of_numbers(num_list,n))

#num_list: [1, 2, 4, 5, 6],n: 10