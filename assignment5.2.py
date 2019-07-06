# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:05:31 2019

@author: Shri
"""

list_of_marks=(24, 24, 24, 24, 24, 24, 24, 25, 24, 24)
#list_of_marks=(25, 25, 3, 0, 0, 0, 25, 25, 0, 1)

def find_more_than_average():
    aggregate=0
    sum=0
    b=[]
    for i in list_of_marks:
        sum=sum+i
    aggregate=sum/(len(list_of_marks))
    for i in list_of_marks:
        if(i > aggregate):
            percentage=(i/25)*100
            b.append(percentage)
    g=(len(b)/len(list_of_marks))*100
    return g
    #Remove pass and write your logic here

def sort_marks():
    b=list(map(int,list_of_marks))
    b.sort()
    return b

def generate_frequency():
    d=[]
    c={}
    for i in range(26):
        values=0
        for j in list_of_marks:
            if(i == j):
               values+=1
               c[i]=values
            else:
                c[i]=values
    for i in c.values():
        d.append(i)
    return d
               



#Variable(list_of_marks-(12, 18, 25, 24, 2, 5, 18, 20, 20, 21))
#Variable(list_of_marks-(12, 18, 25, 24, 2, 5, 18, 20, 20, 21))
#Variable(list_of_marks-(25, 25, 3, 0, 0, 0, 25, 25, 0, 1))	
#Variable(list_of_marks-(24, 24, 24, 24, 24, 24, 24, 25, 24, 24))

    
    

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())