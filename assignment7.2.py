# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:33:27 2019

@author: Shri
"""

Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.

Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Also write the pytest test cases to test the program.

Sample Input	Expected Output
the sun rises in the east	eht snu sesir ni eht stea
