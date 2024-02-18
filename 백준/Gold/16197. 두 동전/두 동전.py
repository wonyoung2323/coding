import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
coin = []
for _ in range(n):
    cc = input()
    arr.append(cc)

for a in range(n):
    for b in range(m):
        if arr[a][b] == 'o':
            coin.append([a, b])

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y, r, s):
    q = deque()
    q.append((x, y, r, s, 0))

    while q:
        xx, yy, rr, ss, cnt = q.popleft()
        if cnt >= 10:
            return -1

        for i in range(4):
            nx = xx + dir[i][0]
            ny = yy + dir[i][1]
            nr = rr + dir[i][0]
            ns = ss + dir[i][1]

            if (0 <= nx < n and 0 <= ny < m) and (0 <= nr < n and 0 <= ns < m):
                if arr[nx][ny] == '#':
                    nx, ny = xx, yy
                if arr[nr][ns] == '#':
                    nr, ns = rr, ss
                q.append((nx, ny, nr, ns, cnt + 1))

            elif (0 <= nx < n and 0 <= ny < m) or (0 <= nr < n and 0 <= ns < m):
                return cnt + 1

            else:
                continue

    return -1


ans = bfs(coin[0][0], coin[0][1], coin[1][0], coin[1][1])
print(ans)