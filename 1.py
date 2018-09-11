# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:41:03 2017

@author: ZHENGHAN ZHANG
"""
import random
#generate 2 lists of 12 random integer values
listMan=[]
listWoman=[]
for i in range(12):
    listMan.append(random.randint(1,10001))
for i in range(12):
    listWoman.append(random.randint(1,10001))
print(listMan,listWoman,sep='\n')    
#employ a numerator 'k', which gains 1 when MAN HAS PROSPEROUS MONTH, and reduce 1 when woman has
m=0
for i in range(12):
    if listMan[i]>listWoman[i]:
        m+=1
    elif listMan[i]<listWoman[i]:
        m-=1
    else:
        continue
if m>0:
    print('The man has more prosperous months.')
elif m<0:
    print('The woman has more prosperous months.')
else:
    print('They both had a good year.')