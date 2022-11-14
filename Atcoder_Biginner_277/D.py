# coding: utf-8
# Your code here!
n=list(map(int,input().split()))
A=list(map(int,input().split()))
A=sorted(A)
if A[0]!=0 or A[-1]!=n[1]-1:
    Max=0
    prev=A[0]
    ans=A[0]
    if n[0]==1:
        print(0)
        exit()
    for i in range(1,len(A)):
        if A[i]==prev:
            ans+=A[i]
        elif A[i]==prev+1:
            ans+=A[i]
            prev=A[i]
        else:
            prev=A[i]
            if Max<ans:
                Max=ans
            ans=A[i]
    if Max<ans:
        Max=ans
    print(sum(A)-Max)
else:
    Max=0
    prev=A[0]
    ans=A[0]
    flag=0
    ans_0=0
    if n[0]==1:
        print(0)
        exit()
    for i in range(1,len(A)):
        if A[i]==prev:
            ans+=A[i]
        elif A[i]==prev+1:
            ans+=A[i]
            prev=A[i]
        else:
            if flag==0:
                ans_0=ans
            flag=1
            prev=A[i]
            if Max<ans:
                Max=ans
            ans=A[i]
        if i==n[0]-1 and flag==1:
            ans+=ans_0
    if Max<ans:
        Max=ans
    print(sum(A)-Max)
