a=list(map(int,input().split()))
H=[]
C=[]
R=[]
Answer=[]
for i in range(a[0]):
    b=list(map(int,input().split()))
    H.append(b)
 
for i in range(a[0]):
    sum_c=0
    for j in range(a[1]):
        sum_c+=H[i][j]
    C.append(sum_c)