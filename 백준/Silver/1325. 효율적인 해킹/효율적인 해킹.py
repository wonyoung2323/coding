import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

def bfs(i):
    ans = 1
    q = deque([i])
    visited = [False] * (n + 1)
    visited[i] = True

    while q:
        cnt = q.popleft()
        
        for e in arr[cnt]:
            if not visited[e]:
                q.append(e)
                ans += 1
                visited[e] = True
    return ans

max_num = 1
result = []

for i in range(1, n + 1):
    num = bfs(i)
    if num > max_num:
        max_num = num
        result.clear()
        result.append(i)
    elif num == max_num:
        result.append(i)

print(*result)