N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
C=sorted(A)
D=sorted(B)

for i in range(N):
    a=abs(C[i]-D[i])
    ans+=a
print(ans)
