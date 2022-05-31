#027 - Sign Up Requests （★2
N=int(input())
A={}
for i in range(N):
    s=input()
    if s not in A.keys():
        print(i+1)
        A[s]=0