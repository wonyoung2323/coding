import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = []
parent = [i for i in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


graph.sort()
answer = 0
for cost, a, b in graph:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union(parent, a, b)
        answer += cost

print(answer)
