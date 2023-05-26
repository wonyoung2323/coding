def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    tmp = [[0] * (M + 1) for _ in range(N + 1)]
    for s in skill:
        r1, c1, r2, c2, degree = s[1], s[2], s[3], s[4], s[5]

        if s[0] == 1:
            tmp[r1][c1] -= degree
            tmp[r1][c2 + 1] += degree
            tmp[r2 + 1][c1] += degree
            tmp[r2 + 1][c2 + 1] -= degree
        elif s[0] == 2:
            tmp[r1][c1] += degree
            tmp[r1][c2 + 1] -= degree
            tmp[r2 + 1][c1] -= degree
            tmp[r2 + 1][c2 + 1] += degree
            
    for i in range(N):
        for j in range(M):
            tmp[i][j + 1] += tmp[i][j]
    
    for i in range(N):
        for j in range(M):
            tmp[i + 1][j] += tmp[i][j]
            
    for i in range(N):
        for j in range(M):
            if board[i][j] + tmp[i][j] > 0:
                answer += 1
            
    return answer