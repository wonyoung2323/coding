import sys
from collections import defaultdict
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))


def R():
    max_len = 0
    for i in range(len(arr)):
        now = defaultdict(int)
        temp = []
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                continue
            now[arr[i][j]] += 1

        now_list = list(now.items())
        now_list.sort(key=lambda x: (x[1], x[0]))
        for j in now_list:
            temp.extend(j)
        arr[i] = temp[:100]
        max_len = max(max_len, len(temp))

    for i in range(len(arr)):
        if len(arr[i]) < max_len:
            arr[i] += [0] * (max_len - len(arr[i]))


count = 0
while True:
    if count > 100:
        print(-1)
        break
    if r - 1 < len(arr) and c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        print(count)
        break

    count += 1
    if len(arr) >= len(arr[0]):
        R()
    else:
        arr = list(map(list, zip(*arr)))
        R()
        arr = list(map(list, zip(*arr)))