# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:22:06 2019

@author: Shri
"""

#Write a python function, check_anagram() which accepts two strings and returns True, 
#if one string is an anagram of another string. Otherwise returns False.

#The two strings are considered to be an anagram if they contain repeating characters 
#but none of the characters repeat at the same position. The length of the strings should be the same.

#Also write the pytest test cases to test the program.

#Note: Perform case insensitive comparison wherever applicable.

#Sample Input	Expected Output
#eat, tea	True
#backward,drawback	False 
#(Reason: character 'a' repeats at position 6, not an anagram)
#Reductions,discounter	True
#About, table	False


def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    p=0
    g=0
    if((len(data1)) == (len(data2))):
        for i in range(len(data1)):
            if(data1[i] == data2[i]):
                p+=1
        if(p == 0):
            for i in range(len(data1)):
                g=0
                for j in range(len(data1)):
                    if(data1[i] == data2[j]):
                        p+=1
                        break
                    else:
                        g+=1
            if(p == len(data1) and g != len(data1)):
                
                return True
            else:
            
                return False
        else:
            
            return False
    else:
        return False
        

print(check_anagram("eat","tea"))

#data2: aab, data1: bca
#data2: Badcredit, data1: Debitcard
#data2: scller, data1: resell	