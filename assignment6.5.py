# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:46:41 2019

@author: Shri
"""




def find_ten_substring(num_str):
    v=[]
    b=list(map(int,num_str))
    for i in range(len(b)-1):
        if(int(b[(i)])+int(b[i+1]) == 10):
            v.append(str(b[i])+str(b[i+1]))
    for i in range(len(b)-2):
        if(int(b[(i)])+int(b[i+1])+int(b[i+2]) == 10):
            v.append(str(b[i])+str(b[i+1])+str(b[i+2]))
    for i in range(len(b)-3):
        if(int(b[(i)])+int(b[i+1]+int(b[i+2])+int(b[i+3])) == 10):
            v.append(str(b[i])+str(b[i+1])+str(b[i+2])+str(b[i+3]))
    return v
    
    
    
    
    
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)

   