import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

ans = INF
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = rgb[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]
    
    dp[n - 1][i] = INF
    now = min(dp[-1])
    ans = min(now, ans)

print(ans)