# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:29:22 2019

@author: Shri
"""

#Assume that a poem is given. Write the regular expressions for the following:
#Print how many times the letter 'v' appears in the poem.
#Remove all the newlines from the poem and print the poem in a single line.
#If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.
#If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*.
#Test your code by using the given sample inputs. 
#Verify your code by using the 2nd sample input(highlighted) given below:
    
    
#If I can stop one heart from breaking,
#I shall not live in vain;
#If I can ease one life the aching,
#Or cool one pain,
#Or help one fainting robin
#Unto his nest again,
#I shall not live in vain.
#4

#If I can stop one heart from breaking, I shall not live in vain; If I can ease one life the aching, Or cool one pain, Or help one fainting robin Unto his nest again, I shall not live in vain. 

#If I can stop one heart from breaking,
#I shall not live in vain;
#If I can ease one life the aChing,
#Or Cool one pain,
#Or help one fainting robin
#Unto his nest again,
#I shall not live in vain.

#If I can stop one heart from breaking,
#I shall not live in vain;
#If I can ease one life the achi*\*
#Or cool one pain,
#Or help one fai*\*ng robin
#Unto hi*\*est again,
#I shall not live in vain.





poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1
import functools
p=0
for i in poem:
    if(i == "v"):
        p+=1
print(p)

print()
b=[]
for i in poem:
    if(i != "\n"):
        b.append(i)
x=functools.reduce(lambda x,y:x+y , b)
print(x)


print()
v=list(map(str,poem))
c=[]
for i in range(len(v)):
    if(v[i] == "c"):
        if(v[i+1] == "o" or v[i+1] == "h"):
            v[i]="C"
            c.append(v[i])
        else:
            c.append(v[i])
    else:
        c.append(v[i])
d=functools.reduce(lambda x,y:x+y , c)
print(d)

#print(#Write your regular expression here for question 3)

#print()
#print(#Write your regular expression here for question 4)
      
