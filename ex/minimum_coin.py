N=int(input())
X=list(map(int,input().split()))
Y=sorted(X)
A,B,C=Y[0],Y[1],Y[2]
ans=10000
k=0
 
for i in range(10000):
    for j in range(10000-i):
        S=A*i+B*j
        if S<=N:
            k=(N-S)//C
            if S+k*C==N:
                ans=min(ans,i+j+k)
print(ans)