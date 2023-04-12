def dfs(v,computers):
    computers[v][v] = 0 
    for i in range(len(computers[v])):
        if computers[v][i] == 1 and computers[i][i] != 0: 
            dfs(i,computers)
    
    
def solution(n, computers):
    answer = 0

    for i in range(n):
        if computers[i][i] == 1: 
            dfs(i,computers)
            answer += 1
    return answer