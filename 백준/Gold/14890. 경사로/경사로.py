"""
list(map(list, zip(*arr)))
"""
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def same(part, c):
    for i in range(1, c):
        if part[i - 1] != part[i]:
            return False
    return True


def isRoad(road):
    if same(road, n):
        return True
    # 경사로 놓았는지 안 놓았는지 확인
    new = [False for _ in range(n)]
    for i in range(1, n):
        #높이 차이가 1보다 큰 경우 지나갈 수 없음
        if abs(road[i] - road[i - 1]) > 1:
            return False

        # 앞쪽이 더 작은 경우 
        if road[i - 1] < road[i]:
            # 낮은 쪽에 경사로 놓을 때 범위가 넘어가는 경우 지나갈 수 없는 길
            if i - l < 0:
                return False
            # 경사로 길이 만큼 높이가 안 같으면 지나갈 수 없음
            if not same(road[i - l : i], l):
                return False
            
            for j in range(i - l, i):
                # 이미 경사로가 놓여있어서 놓을 수 없으면 지나갈 수 없음
                if new[j]:
                    return False
            # 경사로가 다 안 놓여있고, 높이 모든 조건 만족하면 경사로 놓아주기
            new[i - l:i] = [True for _ in range(l)]
            
        elif road[i - 1] > road[i]:
            # 낮은 쪽에 경사로 놓을 때 범위가 넘어가는 경우 지나갈 수 없는 길
            if i + l > n:
                return False
            # 경사로 길이 만큼 높이가 안 같으면 지나갈 수 없음
            if not same(road[i:i + l], l):
                return False
            
            for j in range(i, i + l):
                # 이미 경사로가 놓여있어서 놓을 수 없으면 지나갈 수 없음
                if new[j]:
                    return False
            # 경사로가 다 안 놓여있고, 높이 모든 조건 만족하면 경사로 놓아주기
            new[i:i + l] = [True for _ in range(l)]
        
    return True


ans = 0
for i in range(n):
    if isRoad(arr[i]):
        ans += 1

col_arr = list(map(list, zip(*arr)))
for i in range(n):
    if isRoad(col_arr[i]):
        ans += 1

print(ans)
