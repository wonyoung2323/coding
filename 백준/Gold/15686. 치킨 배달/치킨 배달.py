from itertools import combinations

n, m = map(int, input().split())
city = []
chicken = []
house = []
answer_list = []

for _ in range(n):
    city.append(list(map(int, input().split())))

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

combi_list = list(combinations(chicken, m))

for i in combi_list:
    answer = 0
    for j in house:
        distance = 1e9
        for k in i:
            temp = abs(j[0] - k[0]) + abs(j[1] - k[1])
            distance = min(distance, temp)
        answer += distance
    answer_list.append(answer)

print(min(answer_list))
