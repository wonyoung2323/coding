def solution(a):
    answer = 0
    n = len(a)
    if n == 1:
        answer = 1
    ldp = [0] * n
    rdp = [0] * n
    ldp[0] = a[0]
    rdp[-1] = a[-1]
    
    for i in range(n - 1):
        if ldp[i] < a[i + 1]:
            ldp[i + 1] = ldp[i]
        else:
            ldp[i + 1] = a[i + 1]
    for i in range(n - 1, 1, -1):
        if rdp[i] < a[i - 1]:
            rdp[i - 1] = rdp[i]
        else:
            rdp[i - 1] = a[i - 1]
    
    for i in range(n):
        if a[i] == ldp[i] or a[i] == rdp[i]:
            answer += 1
            
    return answer