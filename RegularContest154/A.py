# coding: utf-8
# Your code here!
n=int(input())
a=int(input())
b=int(input())
if a<b:
    t=a
    a=b
    b=t

a=str(a)
b=str(b)
a=list(a)
b=list(b)
for i in range(n):
    x=int(a[i])
    y=int(b[i])
    if x<y:
        t=a[i]
        a[i]=b[i]
        b[i]=t
a=''.join(a)
b=''.join(b)
print(int(a)*int(b)%998244353)