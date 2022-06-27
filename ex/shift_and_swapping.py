N,Q=map(int,input().split())
A=list(map(int,input().split()))
shift=0
for i in range(Q):
    T,x,y=map(int,input().split())
    if T==3:
        print(A[(x-1-shift)%N])
    elif T==1:
        tmp=A[(x-1-shift)%N]
        A[(x-1-shift)%N]=A[(y-1-shift)%N]
        A[(y-1-shift)%N]=tmp
    else:
        shift+=1

    