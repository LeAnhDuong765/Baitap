# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập giá trị b:"))
if a== 0 and b!= 0:
    print ("phương trình vô nghiệm")
elif a== 0 and b==0:
    print ("phương trình vô số nghiệm")
else:
    print("Nghiệm của phương trình là:",-b/a)