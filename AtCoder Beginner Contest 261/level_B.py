# =list(map(int,input().split()))
# =map(int,input().split())
n = int(input())

A = []
for i in range(n):
    s = list(input().split())
    A.append(s)
for i in range(n):
    for j in range(n):
        if A[i][0][j] == '-':
            continue
        else:
            if A[i][0][j] == 'W':
                if A[j][0][i] != 'L':
                    print('incorrect')
                    exit()
            if A[i][0][j] == 'L':
                if A[j][0][i] != 'W':
                    print('incorrect')
                    exit()
            if A[i][0][j] == 'D':
                if A[j][0][i] != 'D':
                    print('incorrect')
                    exit()
print('correct')
