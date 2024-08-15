# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:07:31 2024

@author: HuynhAnhToan - 23705641
"""

import sympy as sp
x = sp.Symbol('x')
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
equation = sp.Eq(a * x**2 + b * x + c, 0)
solutions = sp.solve(equation, x)
print(f"Nghiệm của phương trình là: {solutions}")