# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:56:22 2024

@author: Student
"""
from random import randint
computer =randint (0,2)
player=input("bạn chọn:")
if computer ==0:
    computer="bao"
    print("computer: bao")
if computer ==1:
    computer="búa"
    print("computer: búa")
if computer ==2:
    computer="kéo"
    print("computer: kéo")
if player=="bao":
    if computer=="bao":
        print("hòa")
    if computer=="búa":
        print("thắng")
    if computer=="kéo":
        print("thua")
if player=="búa":
    if computer=="bao":
        print("thua")
    if computer=="búa":
        print("hòa")
    if computer=="kéo":
        print("thắng")
if player=="kéo":
    if computer=="bao":
        print("thắng")
    if computer=="búa":
        print("thua")
    if computer=="kéo":
        print("hòa")


