import sys
input = sys.stdin.readline

n = int(input())
villiage = []
all = 0

for _ in range(n):
    xi, ai = map(int, input().split())
    villiage.append((xi, ai))
    all += ai

villiage.sort(key=lambda x: (x[0]))

now = 0
ans = 0
for i in range(n):
    now += villiage[i][1]
    if now >= all / 2:
        ans = villiage[i][0]
        break

print(ans)