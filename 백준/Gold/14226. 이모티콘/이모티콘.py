from collections import deque
import sys
input = sys.stdin.readline

s = int(input())

visit = [[False] * (1001) for _ in range(1001)]

def bfs():
    q = deque()
    q.append([1, 0, 0])
    visit[1][0] = True

    while q:
        a, b, time = q.popleft()

        if a == s:
            return time

        for i in range(3):
            if i == 0:
                na, nb = a, a
            elif i == 1:
                na, nb = a + b, b
            else:
                na, nb = a - 1, b

            if na < 0 or na >= 1001 or nb < 0 or nb >= 1001 or visit[na][nb]:
                continue
            visit[na][nb] = True
            q.append([na, nb, time + 1])


print(bfs())