import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    max_num = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if visit[nx][ny] > 0: continue
            if maps[nx][ny] == 'L':
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
                max_num = max(max_num, visit[nx][ny])

    return max_num - 1

result = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)