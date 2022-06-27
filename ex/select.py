#024 - Select +／- One（★2
N,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sabun=0
for i in range(N):
    sabun+=abs(a[i]-b[i])
if sabun==K:
    print("Yes")
elif sabun>K:
    print("No")
elif sabun<K and (K-sabun)%2==0:
    print("Yes")
elif sabun<K and (K-sabun)%2>0:
    print("No")
    