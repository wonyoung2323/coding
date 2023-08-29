import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
gr, gc = -1, -1
for i in range(r):
    for j in range(c):
        if board[i][j] == 'G':
            gr, gc = i, j

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def dfs(a, b, time, crt):
    global visited

    rtn = crt
    if time >= t:
        return rtn

    time += 1
    for d in range(4):
        nr = a + dr[d]
        nc = b + dc[d]

        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            continue
        if board[nr][nc] == '#':
            continue

        if board[nr][nc] == '.':
            rtn = max(rtn, dfs(nr, nc, time, crt))
        elif board[nr][nc] == 'S':
            tmp = board[nr][nc]
            board[nr][nc] = '.'
            rtn = max(rtn, dfs(nr, nc, time, crt + 1))
            board[nr][nc] = tmp

    return rtn


board[gr][gc] = '.'

print(dfs(gr, gc, 0, 0))