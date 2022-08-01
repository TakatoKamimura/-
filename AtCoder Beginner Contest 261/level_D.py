# =list(map(int,input().split()))
n, m = map(int, input().split())
X = list(map(int, input().split()))
dp = [[-1]*(n+1) for i in range(n+1)]
bonus = {}
dp[0][0] = 0
for i in range(m):
    c, y = map(int, input().split())
    bonus[c] = y
for i in range(1, n+1, 1):
    for j in range(n+1):
        if j == 0:
            dp[i][j] = max(dp[i-1])
        else:
            if dp[i-1][j-1] == -1:
                continue
            dp[i][j] = dp[i-1][j-1] + X[i-1]
            if j in bonus:
                dp[i][j] += bonus[j]
print(max(dp[-1]))
