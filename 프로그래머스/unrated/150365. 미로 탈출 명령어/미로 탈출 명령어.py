from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    ds = ['d', 'l', 'r', 'u']
    
    visited = [[[False] * m for _ in range(n)] for _ in range(k + 1)]
    q = deque()
    q.append((x, y, 0, ""))
    visited[0][x][y] = True
    while q:
        xx, yy, kk, ww = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            nk = kk + 1
            nw = ww + ds[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if nk > k : continue
            if visited[nk][nx][ny]: continue
            if nx == r and ny == c and nk == k:
                return nw
            
            visited[nk][nx][ny] = True
            q.append((nx, ny, nk, nw))
        
    return "impossible"