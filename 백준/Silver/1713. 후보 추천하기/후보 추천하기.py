import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
num = int(input())
student = list(map(int, input().split()))
album = defaultdict(list)

order = 0
for i in range(num):
    s = student[i]
    if s in album:
        album[s][0] += 1
    else:
        if len(album) < n:
            album[s] = [1, i]
        else:
            sort_album = sorted(
                album.items(), key=lambda x: (x[1][0], x[1][1]))
            delKey = sort_album[0][0]
            del(album[delKey])
            album[s] = [1, i]

ans = list(album.keys())
ans.sort()
print(' '.join(map(str, ans)))