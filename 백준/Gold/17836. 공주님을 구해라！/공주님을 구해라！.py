from collections import deque

n, m, t = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[int(1e9)] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

gram = int(1e9)


def bfs(a, b):
    global gram
    q = deque()
    q.append((a, b))
    visited[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 2:
                gram = min(gram, visited[x][y] + 1 +
                           (n - 1 - nx) + (m - 1 - ny))
            if arr[nx][ny] == 0 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


bfs(0, 0)
res = min(gram, visited[n - 1][m - 1])
if res <= t:
    print(res)
else:
    print('Fail')