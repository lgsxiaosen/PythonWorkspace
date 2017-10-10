#!/usr/bin/python
# encoding=utf-8

#while输出2~100之间的素数
'''i=2
while(i<100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j+=1
    if(j > (i/j)):
        print i,'是素数'
    i+=1 '''

#for输出2~100之间的素数
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if(j <= (i/j)):
            if not(i%j):
                break
            j+=1
    if(j > (i/j)):
         print i ,'是素数'
    i+=1
