#!/usr/bin/python3
#initialize a list
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
#create two list
A=[]
B=[]
for i in adhoc:
	if i>5 :
	 print(i," is greatr than 5")
	 A.append(i)
	else:
	 print(i," is less than equal to 5")
	 B.append(i)
print("list of no grater than 5:",A)
print("list of no lessthan eq to 5:",B)

