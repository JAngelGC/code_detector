import sys; R = sys.stdin.readline



for _ in range(int(R())):

    dic = {}

    e = [[] for _ in range(6)]

    k = 0

    v = []

    for _ in range(3):

        x1,y1,x2,y2 = map(int,R().split())

        if (x1,y1) not in dic: dic[(x1,y1)] = k; v += (x1,y1),; k += 1

        if (x2,y2) not in dic: dic[(x2,y2)] = k; v += (x2,y2),; k += 1

        p,q = dic[(x1,y1)],dic[(x2,y2)]

        e[p] += q,; e[q] += p,

    if k!=5: print("NO"); continue

    for i in range(5):

        if len(e[i])==2: a = i; break

    b,c = e[a][0],e[a][1]

    x1,y1 = v[a]; x2,y2 = v[b]; x3,y3 = v[c];

    B2,C2 = (x1-x2)**2+(y1-y2)**2,(x1-x3)**2+(y1-y3)**2

    if (x2-x3)**2+(y2-y3)**2>B2+C2: print("NO"); continue

    d,e = sorted(set({0,1,2,3,4})-set({a,b,c}))

    x4,y4 = v[d]; x5,y5 = v[e]

    if (not (x1-x2)*y4+(x2-x4)*y1+(x4-x1)*y2) and (not (x1-x3)*y5+(x3-x5)*y1+(x5-x1)*y3) and \
        B2<=((x1-x4)**2+(y1-y4)**2)*25<=16*B2 and B2<=((x2-x4)**2+(y2-y4)**2)*25<=16*B2 and \
        C2<=((x1-x5)**2+(y1-y5)**2)*25<=16*C2 and C2<=((x3-x5)**2+(y3-y5)**2)*25<=16*C2:
            print("YES"); continue

    if (not (x1-x2)*y5+(x2-x5)*y1+(x5-x1)*y2) and (not (x1-x3)*y4+(x3-x4)*y1+(x4-x1)*y3) and \
        B2<=((x1-x5)**2+(y1-y5)**2)*25<=16*B2 and B2<=((x2-x5)**2+(y2-y5)**2)*25<=16*B2 and \
        C2<=((x1-x4)**2+(y1-y4)**2)*25<=16*C2 and C2<=((x3-x4)**2+(y3-y4)**2)*25<=16*C2:
            print("YES"); continue

    print("NO")