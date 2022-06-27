import statistics
N=int(input())
M=[[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        M[i][j]=(j+1)+(i*N)
for i in range(N-2):
    for j in range(N-2):
        a=M[i][j:j+3]
        a.extend(M[i+1][j:j+3])
        a.extend(M[i+2][j:j+3])
        if M[i+1][j+1]==statistics.median(a):
            tmp=M[i+1][j+1]
            M[i+1][j+1]=M[i+1][j+2]
            M[i+1][j+2]=tmp
for i in range(N):
    s=[]
    for j in range(N):
        s.append(str(M[i][j]))
    print(" ".join(s))