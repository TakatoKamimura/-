# 競プロのやつ
N = int(input())
ruiseki_1 = []
ruiseki_2 = []
ruiseki_1.append(0)
ruiseki_2.append(0)

for i in range(1, N+1, 1):
    n = list(map(int, input().split()))
    if n[0] == 1:
        ruiseki_1.append(ruiseki_1[i-1]+n[1])
        ruiseki_2.append(ruiseki_2[i-1])
    else:
        ruiseki_2.append(ruiseki_2[i-1]+n[1])
        ruiseki_1.append(ruiseki_1[i-1])
Q = int(input())

for j in range(Q):
    q = list(map(int, input().split()))
    x = ruiseki_1[q[1]]-ruiseki_1[q[0]-1]
    y = ruiseki_2[q[1]]-ruiseki_2[q[0]-1]
    print(str(x)+' '+str(y))
