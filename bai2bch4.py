# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:27:40 2024

@author: Student
"""

import math
print("Giải phương trình bậc 2: ax^2 +bx +c=0")
a=float(input("nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
delta=b**2 -4*a*c
if delta<0: 
    print("phương trình vô nghiệm")
elif delta==0:
    x=-b/(2*a) 
    print("có nghiệm khép x1=x2=",x) 
else:
    x1=(-b + math.sqrt(delta))/(2*a) 
    x2=(-b - math.sqrt(delta))/(2*a) 
    print("phương trình có nghiệm kép")
    print("x1:",x1)
    print("x2:",x2)