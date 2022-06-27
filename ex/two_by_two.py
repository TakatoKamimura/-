H,W=map(int,input().split())
A=[]
B=[]
for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)
for i in range(H):
    a=list(map(int,input().split()))
    B.append(a)


C=[]
ans=0

for i in range(H):
    D=[]
    for j in range(W):
        x=B[i][j]-A[i][j]
        ans+=x
        D.append(x)
    C.append(D)
Ans=0
if ans%4==0:
    print('Yes')
    for i in range(H-1):
        for j in range(W-1):
            Ans+=abs(C[i][j])
            C[i][j+1]-=C[i][j]
            C[i+1][j]-=C[i][j]
            C[i+1][j+1]-=C[i][j]
            C[i][j]=0
    print(Ans)
else:
    print('No')