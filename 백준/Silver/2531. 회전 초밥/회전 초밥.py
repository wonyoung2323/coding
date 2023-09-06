import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

sushi += sushi

ans = 0
for i in range(n):
    start = i
    end = i + k
    now = set(sushi[start:end])
    if c in now:
        ans = max(ans, len(now))
    else:
        ans = max(ans, len(now) + 1)

print(ans)