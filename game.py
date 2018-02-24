#!/usr/bin/python
#coding=utf-8
import random

a=random.randint(1,100)
b=input("please input a number from 1 to 100:")
i=0
while a!=b:
	if a>b:
		b=input("your number is small，please input again:")
	else:
		b=input("your number is big ,please input again:")
	i=1+1
else:
	print"congratulations,you have input %d times"% i		
