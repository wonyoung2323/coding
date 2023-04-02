import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

arr = [[INF] * (v+ 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for i in range(1, v + 1):
    for j in range(1, v + 1):
        for k in range(1, v + 1):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

ans = INF
for i in range(1, v + 1):
    ans = min(ans, arr[i][i])

if ans >= INF:
    print(-1)
else:
    print(ans)
