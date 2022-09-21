# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:37:16 2022
@author: MertMM
"""


#Adjustable Parameters

Debt = 42
annualInterestRate = 0.20
monthlyPaymentRate = 0.04
monthsinyear = 12.00

monthlyInterestRate = annualInterestRate / monthsinyear

def minpay(x):
    if x < 1:
        return Debt * monthlyPaymentRate
    else:
        return RemainingBalance(x) * monthlyPaymentRate 

def unpaidBalance(x):
    if x < 0:
        return "Input Error Code #0087: Value for Month has to be greater than or equal to 0"
    else:
        return RemainingBalance(x) - minpay(x)

def CarriedInterest(x):
    if x < 0:
        return "Input Error Code #0054: Month Value provided was less than 0. No interest owed before debt is incurred."
    else:
        return unpaidBalance(x) * monthlyInterestRate

def RemainingBalance(x):
    if x == 0:
        return round(Debt, 2)
    elif x >= 1:
        return round((unpaidBalance(x-1) + CarriedInterest(x-1)), 2)
    else:
        return "Input Error Code #0087: Value for Month has to be greater than or equal to 0."            
