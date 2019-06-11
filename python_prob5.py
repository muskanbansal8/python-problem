#!/usr/bin/pytho3
#taking user name
import time

name=input("enter your name : \n ")
# for check current time in 24 hour clock
ct_time=time.ctime()
parsed=time.strptime(cr_time)
#taking time as a integer
k=int(time.strftime(" %H%M%S ",parsed))
print(k)
if k<115900 & k>50000 :
	print("Good Morning !! ",name)
elif k>120000 & k<165900 :
	print("Good Afternoon !! ",name)
elif k>170000 & k<195900 :
	print("Good Evening !! ",name)
elif k>200000 & k<50000 :
	print("Good Night !! ",name)

