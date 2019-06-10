#!/usr/bin/python3
#now take input from user
name,age=input("enter your name and age with space seprated :").split()
if int(age)<=95:
	year=2019+(95-int(age))
	print(name," you will be 95 years old in ",year)
else:
	year=2019-(int(age)-95)
	print(name,"you was 95 year old in ",year)

