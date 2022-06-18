N=int(input())
Answer=[]
s=0
for i in range(N):
    A=[]
    for j in range(i+1):
        if i==j or j==0:
            A.append(1)
        else:
            s=Answer[i-1][j-1]+Answer[i-1][j]
            A.append(s)
    x=[str(a) for a in A]
    print(' '.join(x))
    Answer.append(A)



    
            
