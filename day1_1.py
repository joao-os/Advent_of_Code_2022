# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:04:30 2022

@author: Joao
"""

import copy as cp

Input1 = open('input1_1.txt', 'r')
Lines = Input1.readlines()
  
current_elf = 0
cals = [0]

fattest_elf = 0
max_cals = 0

for line in Lines:
   
    if (line=="\n"):
            current_elf = current_elf + 1
            cals.append(0)
    else:
        cal = cp.copy(line.replace("\n", ""))
        cal_int = int(cal)
        
        cals[current_elf] = cals[current_elf] + cal_int
    
        if (cals[current_elf] > max_cals):
            max_cals = cals[current_elf]
            fattest_elf = current_elf + 1
    
    