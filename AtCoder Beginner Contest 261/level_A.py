# =list(map(int,input().split()))
L1, R1, L2, R2 = map(int, input().split())
if R1 == L2:
    print(0)
    exit()
if L1 == R2:
    print(0)
    exit()
a = [0]*101
for i in range(L1, R1+1, 1):
    a[i] += 1
for i in range(L2, R2+1, 1):
    a[i] += 1
ans = 0
for i in range(len(a)):
    if a[i] == 2:
        ans += 1
if ans != 0:
    print(ans-1)
else:
    print(0)
