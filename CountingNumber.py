# coding: utf-8
# Your code here!

l,r=map(int,input().split())
n=r-l+1
a=0
b=0
s=1
while(True):
    a+=1
    s=s*10
    if s>l:
        break
s=1
while(True):
    b+=1
    s=s*10
    if s>r:
        break
ans=0
count=1

if a==b:
    print(a*n*(2*l+(n-1))//2%(10**9+7))
    exit()
else:
    while(True):
        if count==1:
            w=10**a
            count+=1
            w=w-l
            ans+=a*w*(2*l+(w-1))//2
            a+=1
        else:
            if a==b:
                w=10**(a-1)
                z=r-w+1
                ans+=a*z*(2*w+(z-1))//2
                break
            else:
                w=10**(a)-10**(a-1)
                z=10**(a-1)
                ans+=a*w*(2*z+(w-1))//2
                a=a+1
print(ans%(10**9+7))
    