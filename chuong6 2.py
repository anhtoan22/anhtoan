# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:32:04 2024

@author: Huỳnh ANh Toàn
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
tong = (a+b)
hieu = (a-b)
tich = (a*b)
if b==0:
    print ("Lỗi phép tính")
chia_nguyen = (a//b)
chia_du = (a%b)
thuong =(a/b)
chia_lay_2_so = round (thuong, 2)
chia_lay_3_so = round (thuong, 3)
print ("Tổng là", tong)
print ("Hiệu là", hieu)
print ("Tích là", tich)
print ("Chia lấy nguyên", chia_nguyen)
print ("Chia lấy dư", chia_du)
print ("Chia lấy 2 số sau dấu phẩy", chia_lay_2_so)
print ("Chia lấy 3 số sau dấu phẩy", chia_lay_3_so)

