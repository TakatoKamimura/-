n,X=map(int,input().split())
a=[]
b=[]
c=[]
s=0
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
    s+=x+y
    c.append(s)
ans=10**30
for i in range(n):
    if X-i<0:
        break
    tmp=c[i]
    tmp=tmp+b[i]*(X-i-1)
    if ans>tmp:
        ans=tmp
print(ans)
    