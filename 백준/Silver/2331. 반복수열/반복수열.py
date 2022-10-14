import sys

def r(A, P, D, C):
    if D.count(A) > 1:
        i = D.index(D[C])
        del D[i:]
        return print(len(D))
    x = [int(a) for a in str(A)]
    temp = 0
    for i in x:
        temp += i ** P
    D.append(temp)
    r(D[C+1], P, D, C+1)

A, P = map(int, sys.stdin.readline().split())
D = [A]
r(A, P, D, 0)