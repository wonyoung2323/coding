import sys
input = sys.stdin.readline

n, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1], x[2]))

dist = [i for i in range(d + 1)]
for s, e, l in arr:
    if e <= d:
        dist[e] = min(dist[e], dist[s] + l)
    for i in range(s, d + 1):
        dist[i] = min(dist[i - 1] + 1, dist[i])

print(dist[d])