# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:51:26 2024

@author: DELL
"""

a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
d=int(input("Nhập d: "))
be_nhat=d
if a>b:
    be_nhat=b
elif a>c:
    be_nhat=c
elif a>d:
    be_nhat=d
else:
    be_nhat=a
print("Số bé nhất là:", be_nhat)