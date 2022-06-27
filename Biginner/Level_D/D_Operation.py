def binary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return mid

N,Q=map(int,input().split())

A=list(map(int,input().split()))
A=sorted(A)

B=[]
Sum=0
for i in range(len(A)):
    Sum+=A[i]
    B.append(Sum)

for i in range(Q):
    k=int(input())
    num=binary_search(A,k)

    if num==0:
        print(B[N-1]-k*N)
    elif num==N-1:
        print(k*N-B[N-1])
    elif A[num]>=k:
        print((k*(num)-B[num-1])+B[N-1]-B[num-1]-k*(N-num))
    elif A[num]<k:
        print((k*(num+1)-B[num])+B[N-1]-B[num]-k*(N-num-1))
    
    #print((k*(num+1)-a)+(b-k*(N-(num+1))))
        
