# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:31:28 2024

@author: Huỳnh Anh Toàn - 23705641
"""
input_string = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = [s.strip() for s in input_string.split(',')]
for sub_string in sub_strings:
    print (sub_string)
