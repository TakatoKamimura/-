import math
X,A,D,N=map(int,input().split())
ans=[]

S=A+(N-1)*D

if D==0:
    print(abs(X-A))
    exit()
if X==A:
    print(0)
    exit()
    
if X<A and D>0:
    print(abs(A-X))
    exit()

if X>A and D<0:
    print(abs(X-A))
    exit()

n=(X-A)//D
n_1=n+1
if n>=N:
    print(abs(X-S))
    exit()

elif n+1>=N:
    print(abs(X-(A+n*D)))
    exit()
    
a=abs(X-(A+n*D))
b=abs(X-(A+n_1*D))
c=min(a,b)
print(c)


    