# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@Author: Huỳnh Anh Toàn - 23705641
"""
GPA = float(input("Nhập điểm trung bình(GPA):"))
if GPA < 3.5:
    print("Học lực Kém")
elif GPA <= 3.5 and GPA <5.0:
    print ("Học lực Yếu")
elif GPA <= 5.0 and GPA <7.0:
    print ("Học lực Trung Bình")
elif GPA <= 7.0 and GPA <8.0:
    print ("Học lực Khá")
elif GPA <= 8.0 and GPA <9.0:
    print ("Học lực Giỏi")
else:
    print ("Học lực Xuất Sắc")
    