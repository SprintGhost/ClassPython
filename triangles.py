#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def triangles():
    L1 = [1],[1,1]
    while True:
        yield L1
        L1.append(0)
        L1 = [x+y for x,y in zip(L1,reversed(L1))]
        



            
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break  
        
        
        
““”
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
        “”“
#杨辉三角的另一种解法
