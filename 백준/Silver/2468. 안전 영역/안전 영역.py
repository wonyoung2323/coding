import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, h):
    visit[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny] == True:
            continue
        if maps[nx][ny] > h and visit[nx][ny] == False:
            visit[nx][ny] = True
            dfs(nx, ny, h)

result = 1
for k in range(max(map(max, maps))):
    visit = [[False] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] > k and not visit[i][j]:
                tmp += 1
                dfs(i, j, k)

    result = max(tmp, result)

print(result)