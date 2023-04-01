import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dp = [[0] * n for _ in range(n)]


def dfs(a, b):
    if dp[a][b] != 0:
        return dp[a][b]

    dp[a][b] = 1
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if area[a][b] < area[nx][ny]:
            dp[a][b] = max(dp[a][b], dfs(nx, ny) + 1)

    return dp[a][b]


ans = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            ans = max(ans, dfs(i, j))

print(ans)