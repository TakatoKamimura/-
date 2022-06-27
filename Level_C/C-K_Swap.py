N, K = list(map(int, input().split()))
a = list(map(int, input().split()))


z = 0
list = []
x_list = []
for i in range(K):
    tmp = []
    x = 0
    if (N-i) % K == 0:
        x = (N-i)//K
    else:
        x = ((N-i)//K)+1
    x_list.append(x)
    for j in range(x):
        tmp.append(a[i+(j*K)])
    tmp = sorted(tmp)
    list.append(tmp)
    # print(tmp)


i = 0
j = 0
past = 0
while(True):
    # print(list[i][j])
    if past > list[i][j]:
        print("No")
        break
    else:
        past = list[i][j]
        i += 1
        if i >= K:
            i = 0
            j += 1
        if j*K+i >= N-1:
            print("Yes")
            break
