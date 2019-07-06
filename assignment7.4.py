# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:35:45 2019

@author: Shri
"""

#In a fair coin we have an equal chance (50%) of either getting a ‘head’ or ‘tail’. 
# That is if we toss the coin a large number of times we would observe head approximately 50% of the time.
# Write a program to implement a biased coin toss where the chance of getting a head is 70% (and tail 30%). That is if we invoke the program 1000 times we should see the head randomly approximately 700 times.


def  biased_coin_toss(num):
    v=int((num/100)*70)
    print("head come" ,v, "time")
    print("tails come",(num-v),"times")
biased_coin_toss(1000)
    
