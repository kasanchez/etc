#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:45:04 2018

@author: kriselle
"""

annual_salary = int(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to be saved as a decimal: '))
monthly_portion_saved = (annual_salary / 12.0) * portion_saved

total_cost = int(input('Enter cost of your dream home: '))
portion_down_payment = .25 * total_cost

current_savings = 0.0
r = .04
months = 0

while current_savings < portion_down_payment:
    months += 1 # += 1 adds 1 to the value and assigns that value to the result sum  
    monthly_return = current_savings * (r/12)
    current_savings += monthly_return + monthly_portion_saved

print("Number of months: ", months)

