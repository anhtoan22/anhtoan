# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:55:04 2024

@author: Huỳnh Anh Toàn - 23705641
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số:"))
if N<10 or N>99:
    print ("Không tồn tại số nguyên dương N")
Chu_so_hang_don_vi = N%10
Chu_so_hang_chuc = N//10
tong = (Chu_so_hang_don_vi + Chu_so_hang_chuc) 
print ("Tổng là", tong)