# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:53:48 2024

@author: Student
"""

a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giác đều")
    elif a==b or b==c or a==c:
        print("Tam giác cân")
    elif a**2==b**2 + c**2 or b**2==a**2 + c**2 or c**2==a**2 + b**2:
        print("Tam giác vuông")
        if a==b or a==c or b==c:
            print("Tam giác vuông cân")
    else:
        print("Tam giác thường")
else:
    print("a,b,c không là 3 cạnh của một tam giác")