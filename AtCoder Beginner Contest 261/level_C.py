# =list(map(int,input().split()))
# =map(int,input().split())
n=int(input())

d={}

for i in range(n):
    s=input()
    if s not in d:
        d[s]=1
        print(s)
    else:
        a=str(d[s])
        d[s]+=1
        s+='('+a+')'
        print(s)
        