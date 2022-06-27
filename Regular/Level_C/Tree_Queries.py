a=1
b=3
A=[]
B=[]
i=-1
n=int(input())
while(True):

    print('? '+str(a),end=' ')
    print(b)
    s=int(input())
    if a==1:
        A.append(s)
        b+=1
    if a==2:
        B.append(s)
        b+=1
        i+=1
    if b==n+1:
        b=3
        a=2
    if a==2 and b==n:
        break
summed = [x + y for (x, y) in zip(A,B)]

count=0
m=1000
for i in range(len(summed)):
    if summed[i]==3:
        count+=1
    if m>summed[i]:
        m=summed[i]
if m!=1:
    print('!'+str(m))
if m==3:
    if count==2:
        print('!3')
    else:
        print('!1')
