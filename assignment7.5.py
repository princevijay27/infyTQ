# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:36:24 2019

@author: Shri
"""

#Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

#Rules are as follows: 
#a. Spaces are to be retained as is 
#b. Each word should be encoded separately

#If a word has only vowels then retain the word as is
#If a word has a consonant (at least 1) then retain only those consonants

#Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

#Sample Input	Expected Output
#I love Python	I lv Pythn
#MSD says I love cricket and tennis too	MSD sys I lv crckt nd tnns t
#I will not repeat mistakes	I wll nt rpt mstks


import functools
def sms_encoding(data):
    b=list(map(str,data))
    b.append(" ")
    v=0
    p=-1
    n=[]
    for i in range(len(b)):
        v+=1
        p+=1
        if(b[i] == " "):
            if((v-1) > 1):
                for j in range(p-(v-1),p):
                    v=0
                    if(b[j] == "a" or b[j] == "e" or b[j] == "i" or b[j] == "o" or b[j] == "u" or b[j]
                    == "A" or b[j] == "E" or b[j] == "I" or b[j] == "O" or b[j] == "U"):
                        n.append(j)
            else:
                v=0
    
    a=-1
    for i in n:
        a+=1
        b.pop(i-a) 
    b.pop(len(b)-1)
    return functools.reduce(lambda x,y:x+y,b)              
    #start writing your code here
  #  b.pop(len(b))
data="GOOD DAYS AND BAD DAYS	"
print(sms_encoding(data))