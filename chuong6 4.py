# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:10:19 2024

@author: Huỳnh Anh Toàn - 23705641
"""
gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
gio_sang_giay = (gio*3600)
phut_sang_giay = (phut*60)
ket_qua_la = (gio_sang_giay + phut_sang_giay + giay)
print ("Kết quả là", ket_qua_la)
                 
