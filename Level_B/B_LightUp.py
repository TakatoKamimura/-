import math

# n = int(input())
N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
# print(l)

max_diff_list = {}
for i in range(N):
    if i+1 in A:
        continue
    max_diff_list[i+1] = 100000000000000000

# max_diff = 0
for a in A:
    tmp = l[a-1]
    for i in range(N):
        if i+1 in A:
            continue
        diff = math.sqrt(abs(tmp[0]-l[i][0])**2+abs(tmp[1]-l[i][1])**2)
        # print(diff)
        if diff < max_diff_list[i+1]:
            max_diff_list[i+1] = diff
        # if diff > max_diff:
        #     max_diff = diff
ans = max(max_diff_list.values())
print(ans)
