n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

result = []

min_result = 1e9
max_result = -1e9

def dfs(add, sub, mul, div, ans, x):
  if add == 0 and sub == 0 and mul == 0 and div == 0:
    result.append(ans)
    return
  
  if add:
    dfs(add - 1, sub, mul, div, ans + data[x], x + 1)
  if sub:
    dfs(add, sub - 1, mul, div, ans - data[x], x + 1)
  if mul:
    dfs(add, sub, mul - 1, div, ans * data[x], x + 1)
  if div:
    if ans > 0:
      dfs(add, sub, mul, div - 1, ans // data[x], x + 1)
    else:
      dfs(add, sub, mul, div - 1, -(-ans // data[x]), x + 1)

dfs(add, sub, mul, div, data[0], 1)
print(max(result))
print(min(result))