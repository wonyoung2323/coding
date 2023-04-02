import sys
import math
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    visit[x][y] = True
    sum = arr[x][y]
    union = [(x, y)]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visit[nx][ny]: continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                union.append((nx, ny))
                visit[nx][ny] = True
                sum += arr[nx][ny]
                q.append((nx, ny))

    for i, j in union:
        arr[i][j] = math.floor(sum / len(union))

    return len(union)


result = 0
while True:
    visit = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1

print(result)