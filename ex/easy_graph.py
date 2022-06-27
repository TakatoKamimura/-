N,M=map(int,input().split())
Answer={}
for i in range(M):
    a,b=map(int,input().split())
    if a<b:
        if b not in Answer:
            Answer[b]=1
        else:
            Answer[b]+=1
    else:
        if a not in Answer:
            Answer[a]=1
        else:
            Answer[a]+=1