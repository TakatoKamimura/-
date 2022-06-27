import numpy as np
a,b,c=map(int,input().split())
d=1
for i in range(b):
    d*=c
if a<d:
    print('Yes')
else:
    print('No')