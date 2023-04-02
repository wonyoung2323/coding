import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
arr = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            arr[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < arr[a][b]:
        arr[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
