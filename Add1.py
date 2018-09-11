# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:04:51 2017

@author: ZHENGHAN ZHANG
"""

##Can use the code from the last exercise::
    #create two strings
x = input('Please enter a binary number: ')
y = input('Please enter another: ')

while True:
    if len(x)>len(y):
        y='0'+y
    elif len(x)<len(y):
        x='0'+x
    else:
        break
    
#loop:core function
'''
0.suppose the first carry is 0
The idea here is two-step:
1.add the two numbers and the previous carry, to have a result
2.decide the new carry [there are three possibilities that have a carry of 1:
    1+1+0, 1+0+1,0+1+1; the rest are all 0]
'''

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
##print(b[:-1])


#binary to decimal
length=len(b)-1
m=0
for i in range(length):
    m+=2**i*int(b[-(i+2)])
    
##print(m)
#check the result
#c=b[:-1]
#print(c)
#print(int(c,2))

##pretty printing:
len3=len(x)-1
lenFinal=len3+3

while x[0]=='0':
    x=x.lstrip('0')
while y[0]=='0':
    y=y.lstrip('0')
    
len1=len(x)-1
len2=len(y)-1
print(' '*(lenFinal-len1+1),x[:-1],sep='')
print('+',' '*(lenFinal-len2),y[:-1],sep='')
print('-'*(lenFinal+1),sep='')
print(' '*4,b[:-1],' = ',m,sep='')    