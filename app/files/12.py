import random
from math import sqrt as s


def dist(x1, y1, x2, y2):
    return s((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_dot_on_line(c1, c2, dot):
    A = c1[1] - c2[1]
    B = c2[0] - c1[0]
    C = c1[0] * c2[1] - c2[0] * c1[1]

    maxx, minx = max(c1[0], c2[0]), min(c1[0], c2[0])
    maxy, miny = max(c1[1], c2[1]), min(c1[1], c2[1])

    res = A * dot[0] + B * dot[1] + C

    if res == 0 and minx <= dot[0] <= maxx and miny <= dot[1] <= maxy:
        return True
    return False


def cosangle(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def same(k11, k12, k21, k22, k31, k32):
    if k11 == k21 or k11 == k22 or k12 == k21 or k12 == k22:
        return 0, 1, 2
    if k11 == k31 or k11 == k32 or k12 == k31 or k12 == k32:
        return 0, 2, 1
    if k21 == k31 or k21 == k32 or k22 == k31 or k22 == k32:
        return 1, 2, 0
    return False


def is_a(c1, c2, c3, debug=-1):
    al = [c1, c2, c3]
    
    lines = same(*c1, *c2, *c3)
    if not lines:
        return False

    c1, c2, c3 = al[lines[0]], al[lines[1]], al[lines[2]]
    if c1[0] == c2[1]:
        c2[0], c2[1] = c2[1], c2[0]
    if c1[1] == c2[0]:
        c1[0], c1[1] = c1[1], c1[0]

    if not (is_dot_on_line(c1[0], c1[1], c3[0]) and is_dot_on_line(c2[0], c2[1], c3[1])):
        if not (is_dot_on_line(c1[0], c1[1], c3[1]) and is_dot_on_line(c2[0], c2[1], c3[0])):
            return False
        c3[0], c3[1] = c3[1], c3[0]

    cosa = cosangle(c1[0][0] - c1[1][0],
                    c1[0][1] - c1[1][1],
                    c2[0][0] - c2[1][0],
                    c2[0][1] - c2[1][1])

    if cosa < 0:
        return False

    l1 = dist(*c1[0], *c3[0]), dist(*c1[1], *c3[0])
    l2 = dist(*c2[0], *c3[1]), dist(*c2[1], *c3[1])

    if min(l1) / max(l1) < 1/4 or min(l2) / max(l2) < 1/4:
        return False

    return True
                                                                                                                                                                                                                                            

n = int(input())
for i in range(n):
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    if is_a([c1[:2], c1[2:]], [c2[:2], c2[2:]], [c3[:2], c3[2:]], debug=i):
        print("YES")
    else:
        print("NO")
