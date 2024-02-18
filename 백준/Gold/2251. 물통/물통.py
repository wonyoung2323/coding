import sys
from collections import deque
input = sys.stdin.readline


def pour(p, q, pp):
    if p + q > pp:
        s = pp
        r = q - (pp - p)
    else:
        s = p + q
        r = 0

    return s, r


def bottle(a, b, c):
    q = deque()
    q.append((0, 0, c))
    case.add((0, 0, c))

    while q:
        na, nb, nc = q.popleft()

        if na < a:
            if nb > 0:
                aa, bb = pour(na, nb, a)
                if (aa, bb, nc) not in case:
                    q.append((aa, bb, nc))
                    case.add((aa, bb, nc))
            if nc > 0:
                aa, cc = pour(na, nc, a)
                if (aa, nb, cc) not in case:
                    q.append((aa, nb, cc))
                    case.add((aa, nb, cc))

        if nb < b:
            if na > 0:
                bb, aa = pour(nb, na, b)
                if (aa, bb, nc) not in case:
                    q.append((aa, bb, nc))
                    case.add((aa, bb, nc))
            if nc > 0:
                bb, cc = pour(nb, nc, b)
                if (na, bb, cc) not in case:
                    q.append((na, bb, cc))
                    case.add((na, bb, cc))

        if nc < c:
            if na > 0:
                cc, aa = pour(nc, na, c)
                if (aa, nb, cc) not in case:
                    q.append((aa, nb, cc))
                    case.add((aa, nb, cc))
            if nb > 0:
                cc, bb = pour(nc, nb, c)
                if (na, bb, cc) not in case:
                    q.append((na, bb, cc))
                    case.add((na, bb, cc))


a, b, c = map(int, input().split())
case = set()

bottle(a, b, c)

ans = set()
for q, w, e in case:
    if q == 0:
        ans.add(e)

print(*sorted(list(ans)))