# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:44:10 2019

@author: Shri
"""

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    b=[]
    for i in patient_medical_speciality_list:
        if(type(i) == str):
            for j in medical_speciality.keys():
                 if(i == j):  
                   b.append(i)
    print(b)
    c={}
    
    for i in b:
        value=0
        for j in b:
            if(i == j):
               value+=1
               c[i]=value
    a=max(c.keys(), key=(lambda k: c[k]))
    speciality = medical_speciality[a] 
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)