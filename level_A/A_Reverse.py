L,R=map(int,input().split())
S=list(input())
S_t=S[L-1:R]

for i in range(L-1,R,1):
    t=i-(L-1)+1
    S[i]=S_t[-t]
print(''.join(S))
    