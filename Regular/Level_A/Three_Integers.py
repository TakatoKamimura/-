a=list(map(int,input().split()))
if a[0]==a[1] and a[1]==a[2]:
    print(a[0])
    exit()
a=sorted(a)
m=a[-1]
b=[]
for i in range(3):
    b.append(a[i]-m)
b=sorted(b)

if b[0]==b[1]:
    if a[0]>0:
        print(m)
        exit()
    else:
        print(-1)
        exit()
else:
    if abs(b[1])>a[0]:
        print(-1)
        exit()
    else:
        print(m)
        exit()