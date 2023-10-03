import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(person, cnt):
    global ans
    visited[person] = True
    if cnt >= 5:
        ans = 1
        return

    for i in graph[person]:
        if not visited[i]:
            dfs(i, cnt + 1)
    visited[person] = False


ans = 0
visited = [False] * n
for i in range(n):
    dfs(i, 1)

print(ans)