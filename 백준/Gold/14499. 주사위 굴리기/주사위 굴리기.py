import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1] 
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    up, back, east, west, front, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:
        dice[0], dice[2], dice[3], dice[5] = east, down, up, west
    if dir == 2:
        dice[0], dice[2], dice[3], dice[5] = west, up, down, east
    if dir == 3:
        dice[0], dice[1], dice[4], dice[5] = back, down, up, front
    if dir == 4:
        dice[0], dice[1], dice[4], dice[5] = front, up, down, back

for i in range(k):
    nx = x + dx[command[i]]
    ny = y + dy[command[i]]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    turn(command[i])
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0])