# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:23:06 2019

@author: Shri
"""

#Write a python program that accepts a text and displays a string which contains the word with 
#the largest frequency in the text and the frequency itself separated by a space.

#Rules:
#The word should have the largest frequency.
#In case multiple words have the same frequency, then choose the word that has the maximum length.
#Assumptions:
#The text has no special characters other than space.
#The text would begin with a word and there will be only a single space between the words.
#Perform case insensitive string comparisons wherever necessary.

#Sample Input	Expected Output
#"Work like you do not need money love like you have never been hurt and dance like no one is watching"	like 3
#"Courage is not the absence of fear but rather the judgement that something else is more important than fear"	fear 2


import functools
def max_frequency_word_counter(data):
    data=data.lower()
    data=(data+" ")
    word=""
    frequency=0
    c={}
    v=0
    g=0
    b=[]
    for i in data:
    
        if(i != "," and i != " "):
          b.append(i)
        elif(i == " "):
            p=0
            v=functools.reduce(lambda x,y:x+y , b)
            del b[:]
            for j in data:
                if(j != "," and j != " "):
                    b.append(j)
                elif(j == " "):
                    g=functools.reduce(lambda x,y:x+y , b)
                    del b[:]
                    if(v == g):
                        p+=1
                        if(p>1):
                            c[v]=p
    p=[]
    f={}
    p=0     
    h=0
    for key,value in c.items():
        p=0
        for j in c.values():
            if(value == j):
               p+=1
            if(p>1):
               b.append([key,value])
               
    if(b == []):
        h=max(zip(c.values(),c.keys()))
        for i in h:
            if(type(i) == str):
                word=i
        frequency=c[word]
  
    elif(b != []):
        for i in range(len(b)):
            p=0
            for j in str(b[i][i-i]):
               p+=1
               f[str(b[i][0])]=p
        h=max(zip(f.values(),f.keys()))
        for i in h:
           if(type(i) == str):
                word =i
        
        frequency=c[word] 
  
    print(word,frequency) 
    
        
        
        
                    
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money love like you have never been hurt and dance like no one is watching"
max_frequency_word_counter(data)