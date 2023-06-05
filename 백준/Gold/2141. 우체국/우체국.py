N = int(input())

count = 0
li = []
for i in range(N):
    a, b = map(int, input().split())
    li.append([a, b])
    count += b

li.sort()

target = count / 2
sum_ = 0
for i in li:
    sum_ += i[1]
    if sum_ >= target:
        print(i[0])
        break
