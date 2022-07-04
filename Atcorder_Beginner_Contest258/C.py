n,q=map(int,input().split())
s=input()
shift=0

for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        shift+=Q[1]
    else:
        print(s[(Q[1]-1-shift)%n])