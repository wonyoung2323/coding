import sys
input = sys.stdin.readline

def show():
    print("---------------------")
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=' ')
        print()

def dust():
    new = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            spread = arr[i][j] // 5
            if arr[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        new[nx][ny] += spread
                        arr[i][j] -= spread                   
                    
    for i in range(r):
        for j in range(c):
            arr[i][j] += new[i][j]

    #show()


def upper():
    dir_x = [0, -1, 0, 1]
    dir_y = [1, 0, -1, 0]

    dir = 0   
    x = air1
    y = 1

    temp = arr[x][y]

    while True:
        nx = x + dir_x[dir]
        ny = y + dir_y[dir]

        if nx == air2 and ny == 0: break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        arr[x][y], temp = temp, arr[x][y]
        x, y = nx, ny

    arr[air1][1] = 0

def down():
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]

    dir = 0   
    x = air2
    y = 1

    temp = arr[x][y]

    while True:
        nx = x + dir_x[dir]
        ny = y + dir_y[dir]

        if nx == air1 and ny == 0: break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        arr[x][y], temp = temp, arr[x][y]
        x, y = nx, ny

    arr[air2][1] = 0

r, c, t = map(int, input().split())
arr = []

for _ in range(r):
    arr.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(r):
    if arr[i][0] == -1:
        air1 = i
        air2 = i + 1
        break

while(t > 0):
    t -= 1
    #미세먼지 확산
    dust()
    upper()
    down()

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            ans += arr[i][j]

#show()
print(ans)