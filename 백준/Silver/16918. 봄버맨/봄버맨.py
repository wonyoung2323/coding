import sys
from copy import deepcopy
input = sys.stdin.readline


def print_board():
    for i in range(r):
        print(''.join(board[i]))


def time_plus(board, time, r, c):
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                time[i][j] += 1


def set_bomb(board, time, r, c):
    for i in range(r):
        for j in range(c):
            if board[i][j] != 'O':
                board[i][j] = 'O'
                time[i][j] = 1


def bomb(board, time, r, c):
    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)
    tmp_time = deepcopy(time)
    for i in range(r):
        for j in range(c):
            if tmp_time[i][j] >= 3:
                board[i][j] = '.'
                time[i][j] = 0
                for k in range(4):
                    rr = i + dx[k]
                    cc = j + dy[k]
                    if rr < 0 or rr >= r or cc < 0 or cc >= c:
                        continue
                    board[rr][cc] = '.'
                    time[rr][cc] = 0


r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
time = [[0] * c for _ in range(r)]

time_plus(board, time, r, c)

for t in range(2, n + 1):
    time_plus(board, time, r, c)
    if t % 2 == 0:
        set_bomb(board, time, r, c)
    if t % 2 == 1:
        bomb(board, time, r, c)

print_board()