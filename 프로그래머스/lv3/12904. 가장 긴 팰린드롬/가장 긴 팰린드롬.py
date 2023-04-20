'''
    a   b   a   c   d   e
a   1   0   0   0   0   0
b   0   1   0   0   0   0
a   0   0   1   0   0   0
c   0   0   0   1   0   0
d   0   0   0   0   1   0
e   0   0   0   0   0   1
'''
def solution(s):
    answer = 1
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            answer = 2
    for i in range(2, n):
        for j in range(n - i):
            if s[j] == s[i + j] and dp[j + 1][i + j - 1] == 1:
                dp[j][i + j] = 1
                answer = max(answer, i + 1)         

    return answer