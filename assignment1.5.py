# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:12:42 2019

@author: Shri
"""


mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False

total=0
total_distance_cover = (distance_one_way*2)
total_cost = (total_distance_cover/mileage)*amount_per_litre
cost_per_head = (total_cost/4)
per_head_cost = str(cost_per_head)

if(cost_per_head%5 == 0):
    divisible_by_five = True
else:
    divisible_by_five=False

print(per_head_cost)
print(divisible_by_five)