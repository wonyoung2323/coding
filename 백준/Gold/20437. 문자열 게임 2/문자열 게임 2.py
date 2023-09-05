import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    cnt = defaultdict(list)
    for i in range(len(w)):
        cnt[w[i]].append(i)

    minVal = int(1e9)
    maxVal = -int(1e9)
    for key, val in cnt.items():
        nowLen = len(val)
        if nowLen >= k:
            for i in range(nowLen - k + 1):
                minVal = min(minVal, val[i + k - 1] - val[i] + 1)
                maxVal = max(maxVal, val[i + k - 1] - val[i] + 1)
    if minVal == int(1e9) or maxVal == -int(1e9):
        print(-1)
    else:
        print(minVal, maxVal)