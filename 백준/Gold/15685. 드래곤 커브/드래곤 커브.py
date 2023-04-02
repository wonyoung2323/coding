"""
0 0 (1 0) => (x y*-1) => (y*-1 x)
0   0 0, 1 0
1   0 0, 1 0, 1 -1 (-1 0, 0 -1)
2   0 0, 1 0, 1 -1, 0 -1, 0 -2 (-1 1, 0 1, -1 0, -1 -1)
3   0 0, 1 0, 1 -1, 0 -1, 0 -2, -1 -2, -1 -1, -2 -1

4 2 (0, -1)
0   4 2, 4 1
1   4 2, 4 1, 3 1 (0 1, -1 0)
2   4 2, 4 1, 3 1, 3 2, 2 2 (1 1, 1 0, 0 1, -1 1)
3   4 2, 4 1, 3 1, 3 2, 2 2, 2 3, 3 3

"""
import sys
input = sys.stdin.readline

n = int(input())
dragon = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    curve = []
    x, y, d, g = map(int, input().split())
    curve.append((x, y))
    curve.append((x + dx[d], y + dy[d]))
    if g > 0:
        for _ in range(g):
            l = len(curve)
            for i in range(1, l):
                nx = curve[l - 1 - i][0] - curve[l - 1][0]
                ny = curve[l - 1 - i][1] - curve[l - 1][1]

                curve.append((curve[l - 1][0] - ny, curve[l - 1][1] + nx))

    dragon.extend(curve)

dragon_set = set(dragon)
dragon_curve = list(dragon_set)
# print(dragon_curve)

ans = 0
for d in range(len(dragon_curve)):
    sx = dragon_curve[d][0]
    sy = dragon_curve[d][1]

    if (sx + 1, sy) not in dragon_curve:
        continue
    if (sx, sy + 1) not in dragon_curve:
        continue
    if (sx + 1, sy + 1) not in dragon_curve:
        continue

    ans += 1

print(ans)