# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:59:21 2024

@author: DELL
"""

a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
d=int(input("Nhập d: "))
lon_nhat=d
if a<b:
    lon_nhat=b
elif a<c:
    lon_nhat=c
elif a<d:
    lon_nhat=d
else:
    lon_nhat=a
print("Số lớn nhất là:", lon_nhat)