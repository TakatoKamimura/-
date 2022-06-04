N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A_dic={}
B_dic={}
C_dic={}
for i in range(46):
    A_dic[i]=0
    B_dic[i]=0
    C_dic[i]=0


for i in range(N):
    A_dic[A[i]%46]+=1
    B_dic[B[i]%46]+=1
    C_dic[C[i]%46]+=1
ans=0

for i in range(46):
    for j in range(46):
        if A_dic[i]>0 and B_dic[j]>0:
            s=(i+j)%46
            if C_dic[(46-s)%46]>0:
                ans+=A_dic[i]*B_dic[j]*C_dic[(46-s)%46]
print(ans)