X,Y=map(int,input().split())
count=0
while(True):
    if X>=Y:
        break
    X=X+10
    count+=1
print(count)