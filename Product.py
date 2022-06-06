N,X=map(int,input().split())

A=(list(map(int,input().split())))
B=[x for x in A[1:] if X%x==0]
B.insert(0,A[0])
Answer=[]
for i in range(N-1):
    A=list(map(int,input().split()))
    C=[]
    if i==0:
        for j in range(len(B)-1):
            for k in range(len(A)-1):
                if X%(B[j+1]*A[k+1])==0:
                    Answer.append(B[j+1]*A[k+1])
    else:
        for j in range(len(Answer)):
            for k in range(len(A)-1):
                if X%(Answer[j]*A[k+1])==0:
                    C.append(Answer[j]*A[k+1])
        Answer=C
count=0

for i in range(len(Answer)):
    if Answer[i]==X:
        count+=1
        
print(count)



            



    
