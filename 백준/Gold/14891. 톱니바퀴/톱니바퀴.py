'''
n극 0, s극 1
1 시계, -1 반시계
'''
import sys
input = sys.stdin.readline

wheels = []
for _ in range(4):
    w = list(map(int, input().rstrip()))
    wheels.append(w)


def check_dir(n, d):
    dir = [0] * 4
    dir[n] = d

    for i in range(n, 0, -1):
        if wheels[i][6] == wheels[i - 1][2]:
            break
        dir[i - 1] = dir[i] * (-1)

    for i in range(n, 3):
        if wheels[i][2] == wheels[i + 1][6]:
            break
        dir[i + 1] = dir[i] * (-1)
    return dir


def clock(wheel):
    new = [0] * 8
    for i in range(8):
        new[i] = wheel[(i + 1) % 8]
    return new


def rclock(wheel):
    new = [0] * 8
    new[0] = wheel[7]
    for i in range(1, 8):
        new[i] = wheel[i - 1]
    return new


k = int(input())
r = []
for _ in range(k):
    n, d = map(int, input().split())
    dir = check_dir(n - 1, d)
    for i in range(4):
        if dir[i] == 1:
            wheels[i] = rclock(wheels[i])
        elif dir[i] == -1:
            wheels[i] = clock(wheels[i])

ans = 0
for i in range(4):
    if wheels[i][0] == 1:
        ans += 2 ** i

print(ans)