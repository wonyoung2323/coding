from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    w = input().rstrip()
    temp = 0
    for i in w:
        temp |= 1 << (ord(i) - ord('a'))
    words.append(temp)

ans = 0
target = (1 << 26) - 1
for i in range(1, n + 1):
    combi = combinations(words, i)
    for c in combi:
        temp = 0
        for cc in c:
            temp |= cc
        if temp == target:
            ans += 1

print(ans)