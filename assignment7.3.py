# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:34:59 2019

@author: Shri
"""

#Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
#The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

#The function should identify the degree of correctness as mentioned below:
#CORRECT, if it is an exact match

#ALMOST CORRECT, if no more than 2 letters are wrong
#WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

#and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
#Assume that the words contain only uppercase letters and the maximum word length is 10.


#Also write the pytest test cases to test the program.


#Sample Input	Expected Output
#{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}	[2, 2, 1]
import functools
def find_correct(word_dict):
    c=list(functools.reduce(lambda x,y:x+y , word_dict.items()))
    value=0
    b=0
    p={"CORRECT":0,"ALMOST CORRECT":0,"WRONG":0}
    z=0
    l=0
    q=0
    for i in range(int(len(c)/2)):
        b=0
        for j in range(len(c[i+value])):
            for k in range(len(c[i+value+1])):
                 if(j==k):
                     if(c[i+value][j]==c[i+value+1][k]):
                            b+=1
                   
        if(len(c[i+value]) == b):
            z+=1
            p["CORRECT"]=z
       
        elif((len(c[i+value])-1) == b or (len(c[i+value])-2) == b):
            l+=1           
            p["ALMOST CORRECT"]=l
        else:
            q+=1
            p["WRONG"]=q
        value+=1
    n=list(map(int,p.values()))
    return n        
    #start writing your code here

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))


#{POLICY: POLICY, WIND: WIPE, WELCOME: WELL}
#{"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
#{WHIZZY: MIZZLY, PRETTY: PRESEN}	
#word_dict-{RISE: RISES}	

