import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

while True:
    if t[-1] == 'A':
        t = t[0:-1]
    elif t[-1] == 'B':
        t = t[0:-1]
        t = t[::-1]

    if len(t) <= len(s):
        if t == s:
            print(1)
        else:
            print(0)
        break