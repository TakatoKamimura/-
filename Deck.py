Q=int(input())
Y=[]
for i in range(Q):
    t,x=map(int,input().split())
    if t==1:
        Y.append(x)
    if t==2:
        Y.insert(0,x)
    if t==3:
        print(Y[len(Y)-x])