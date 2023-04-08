import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(a, b):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    q.append((a, b))
    visited[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    return visited


n, m, energy = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
person = []
dest = []
for i in range(m):
    a, b, c, d = map(int, input().split())
    person.append((a - 1, b - 1))
    dest.append((c - 1, d - 1))

possible = True
while person:
    min_person = []
    check = bfs(sx, sy)
    for i in range(len(person)):
        min_person.append(
            (check[person[i][0]][person[i][1]], person[i][0], person[i][1], i))
    min_person.sort(key=lambda x: (x[0], x[1], x[2]))
    pl, px, py, idx = min_person.pop(0)
    if pl == -1:
        possible = False
        break
    if energy - pl < 0:
        possible = False
        break
    energy -= pl
    go = bfs(px, py)
    use_energy = go[dest[idx][0]][dest[idx][1]]
    if energy - use_energy < 0:
        possible = False
        break
    energy += use_energy
    sx, sy = dest[idx][0], dest[idx][1]
    del person[idx]
    del dest[idx]

if possible:
    print(energy)
else:
    print(-1)