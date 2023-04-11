import sys
input = sys.stdin.readline

n = int(input())
# arr = []
max_dp = [0] * 3
min_dp = [0] * 3
for i in range(n):
    a, b, c = map(int, input().split())

    if i == 0:
        max_dp[0] = min_dp[0] = a
        max_dp[1] = min_dp[1] = b
        max_dp[2] = min_dp[2] = c
    else:
        max_0 = max(max_dp[0], max_dp[1]) + a
        min_0 = min(min_dp[0], min_dp[1]) + a

        max_1 = max(max_dp[0], max_dp[1], max_dp[2]) + b
        min_1 = min(min_dp[0], min_dp[1], min_dp[2]) + b

        max_2 = max(max_dp[1], max_dp[2]) + c
        min_2 = min(min_dp[1], min_dp[2]) + c

        max_dp = [max_0, max_1, max_2]
        min_dp = [min_0, min_1, min_2]  

print(max(max_dp), min(min_dp))