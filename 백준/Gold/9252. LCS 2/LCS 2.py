import sys
input = sys.stdin.readline

a = [""] + list(input().strip())
b = [""] + list(input().strip())

len_a = len(a)
len_b = len(b)
dp = [[""] * len_b for _ in range(len_a)]

for i in range(1, len_a):
    for j in range(1, len_b):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

result = dp[-1][-1]
print(len(result))
print(result)
