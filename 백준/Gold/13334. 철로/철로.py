import heapq as h

N = int(input())
people = []

for i in range(N):
    ele = list(map(int, input().split()))
    ele.sort()
    people.append(ele)
L = int(input())

people.sort(key=lambda x : (x[1], x[0]))

end = people[0][1]
start = end - L
hq = []
answer = 0
count = 0
for i in people:
    if i[1] - i[0] > L:
            continue
    if i[0] >= start and i[1] <= end:
        count += 1
        answer = max(answer, count)
        h.heappush(hq, i)
    elif i[1] > end:
        end = i[1]
        start = end - L
        count += 1
        h.heappush(hq, i)
        while hq and hq[0][0] < start:
            h.heappop(hq)
            count -= 1
        answer = max(answer, count)
        

print(answer)