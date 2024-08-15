# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:05:06 2024

@author: Huỳnh Anh Toàn -23705641
"""

import sympy as sp
x = sp.Symbol('x')
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
equation = sp.Eq(a * x + b, 0)
solution = sp.solve(equation, x)
print(f"Nghiệm của phương trình là: {solution[0]}")