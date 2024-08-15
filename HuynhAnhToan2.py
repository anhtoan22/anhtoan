# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:10:08 2024

@author: Huỳnh Anh Toàn - 23705641
"""
def xác_định_tam_giác(a, b, c):
    sides = sorted([a, b, c]) 
    a, b, c = sides
    if a + b <= c:
        return "Đây không phải là tam giác"    
    if a == b == c:
        return "Tam giác đều"
    elif a**2 + b**2 == c**2:
        return "Tam giác vuông"
    elif a == b or b == c:
        return "Tam giác cân"
    else:
        return "Tam giác thường"
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
result = xác_định_tam_giác(a, b, c)
print(result)

