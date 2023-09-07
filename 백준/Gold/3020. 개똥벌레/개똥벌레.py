import sys
input = sys.stdin.readline

n, h = map(int, input().split())

caves = [0] * (h + 1)

for i in range(n):
    a = int(input())
    if i % 2 == 0:
        caves[0] += 1
        caves[a] -= 1
    else:
        caves[h] -= 1
        caves[h - a] += 1

cnt = 0
for i in range(1, h + 1):
    caves[i] = caves[i] + caves[i - 1]

ans = min(caves[:h])
for i in range(h):
    if caves[i] == ans:
        cnt += 1

print(ans, cnt)