import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
m = n * 2
robot = deque([0] * n)

cnt = 1
while True:
    a.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1]  == 0 and a[i + 1] >= 1:
            a[i + 1] -= 1
            robot[i + 1] = robot[i]
            robot[i] = 0
    robot[-1] = 0
    if robot[0] == 0 and a[0] > 0:
        robot[0] = 1
        a[0] -= 1

    if a.count(0) >= k:
        print(cnt)
        break   
    cnt += 1