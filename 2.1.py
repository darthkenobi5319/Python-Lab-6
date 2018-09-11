# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:58:10 2017

@author: ZHENGHAN ZHANG
"""

#create two strings
x = '01'
y = '10'
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