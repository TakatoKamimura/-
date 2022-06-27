a = list(map(int, input().split()))
def base10int(value, base):
    if (value // base):
        return base10int(value // base, base) + str(value % base)
    return str(value % base)
    
N=a[0]
k=a[1]
 
for i in range(k):
    x=int(str(N),8)
    x_9=list(base10int(x, 9))
    for j in range(len(x_9)):
        if x_9[j]=='8':
            x_9[j]='5'