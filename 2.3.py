# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:53:13 2017

@author: ZHENGHAN ZHANG
"""

#create two strings
x = '10101'
y = '1010'
while True:
    if len(x)>len(y):
        y='0'+y
    elif len(x)<len(y):
        x='0'+x
    else:
        break
#loop:core function
x+='0'
y+='0'
b=''
carry=bool(0)
for i in range(len(x)):
    k=-(i+1)    
    result=bool(int(x[k]))^bool(int(y[k]))^carry
    if bool(int(x[k])) and bool(int(y[k])):
        carry=bool(1)
    elif bool(int(x[k])) and carry:
        carry=bool(1)
    elif bool(int(y[k])) and carry:
        carry=bool(1)
    else:
        carry=bool(0)
    b=str(int(result))+b
b=str(int(carry))+b
while b[0]=='0':
    b=b.lstrip('0')
print(b[:-1])

#binary to decimal
length=len(b)-1
m=0
for i in range(length):
    m+=2**i*int(b[-(i+2)])
print(m)
#check the result
c=b[:-1]
print(c)
print(int(c,2))
    