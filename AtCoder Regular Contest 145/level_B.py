line = input().split(" ")
N = int(line[0])
A = int(line[1])
B = int(line[2])
count = 0
count2 = 0

if A > N:
    print(0)
elif B > N:
    print(N-A+1)
elif A == B:
    print(N-A+1)
else:
    if A > B:
        print((B)*((N//A)-1)+min(B-1, N-A*(N//A))+1)
    else:
        print(N-A+1)
