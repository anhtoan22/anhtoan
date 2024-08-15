# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:34:54 2024

@author: DELL
"""
x = float(input("Số km đã đi (km):"))
if x <= 1: 
    print ("Số tiền là 20000")
elif 1 < x <= 3:
    print (("Số tiền là"), x*13000)
elif 3 < x <= 8:
    print (("Số tiền là"),39000 + (x-3)*12000)
else:
    print(("Số tiền là"),(100000 + (x-8)*10000)*0.92)



