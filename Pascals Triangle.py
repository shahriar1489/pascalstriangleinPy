# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:21:39 2018

@author: Shahriar 
"""

n = 10 # height of triangle
li = [[1]] # empties list 
temp = []

for i in range(0, n): 
    #print('$', end='') # works 
    temp.append(1)
    
    for j in range(1, len(li[i])):
        temp.append( li[i][j-1] + li[i][j] )
    
    temp.append(1)
    li.append(temp)
    temp = []
    
    
#print the pascal's triangle
for i in range(n):    
    # print the spaces here 
    for k in range(n, i, -1):
        print(' ', end='')
    
    
    for j in range(len(li[i])):
        print(li[i][j], end=' ')
    print()
