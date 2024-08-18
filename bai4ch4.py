# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:14:26 2024

@author: Student
"""
print("Tính tiền taxi theo số km quãng đường đi được")
d=float(input("Nhập quãng đường đã đi:"))
if d==1:
    t=20
    print("Tiền taxi là:",t)
elif d>1 and d<3:
    t=13*d
    print("Tiền taxi là:",t)
elif d>=4 and d<=8:
    t=3*13 + (d-3)*12
    print ("Tiền taxi là:",t)
else:
    t=39 + 60 + (d-8)*10
    p=t*0.92
    print("Tiền taxi sau khi giảm:",p)