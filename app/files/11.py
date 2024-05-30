""" A : Determine if three line segments form A """


def cross(vecA, vecB):
    return vecA[0] * vecB[1] - vecA[1] * vecB[0]


def dot(vecA, vecB):
    return vecA[0] * vecB[0] + vecA[1] * vecB[1]


def angle(lineA, lineB):
    x1, y1 = (lineA[0][0] - lineA[1][0], lineA[0][1] - lineA[1][1])
    x2, y2 = (lineB[0][0] - lineB[1][0], lineB[0][1] - lineB[1][1])
    d1 = (x1 ** 2 + y1 ** 2) ** 0.5
    d2 = (x2 ** 2 + y2 ** 2) ** 0.5
    return (x1 * x2 + y1 * y2) / (d1*d2)


def div_ratio(line, point):
    # Simple way to approximately check if the point lies on the line
    mx, my = point
    (a, b), (c, d) = line
    if not (min(a, c) <= mx <= max(a, c) and min(b, d) <= my <= max(b, d)): 
        return -1
    
    # Again make sure the point lies on the line
    vecA = (a - mx, b - my)
    vecB = (a - c, b - d)
    if cross(vecA, vecB) != 0: 
        return -1

    # Finally compute the ratio
    if c == a and d == b: return -1
    if d != b:
        ratio = (my - b) / (d - b)
    if a != c:
        ratio = (mx - a) / (c - a)
    if ratio < 0.2 or ratio > 0.8: 
        ratio = -1
    return ratio
    
def isA(lines):
    """ Given three line segments check if they form A of not"""

    # Find the two slanted line segments
    k, l = -1, -1
    lines_found = False
    for i in range(3):
        if lines_found: break
        temp = set(lines[i])
        for j in range(i + 1, 3):
            # Check which of the two points is the common point
            if lines[j][0] in temp:
                common = lines[j][0]
                k, l = i, j
                lines_found = True
                break

            if not lines_found and lines[j][1] in temp:
                common = lines[j][1]
                k, l = i, j
                lines_found = True
                break
    
    if not lines_found: return False
    
    # Process the lines
    lineA = lines[k]
    if lineA[0] != common:
        lineA = [lineA[1], lineA[0]]

    lineB = lines[l]
    if lineB[0] != common:
        lineB = [lineB[1], lineB[0]]

    # Check the angle between two lines. Must be greater than 0 and less than 90
    degree = angle(lineA, lineB)
    # print("Degree ", degree)
    if degree < 0 or degree >= 1: return False

    # The third is the line connecting two slanted line segments
    divider = lines[3 - k - l]

    # If first point of divider does not divide (or lie on) either of the line segments, it does not form A
    thresh = 0.2 # Converted 1/4 to 1/5 in another metric
    r1 = div_ratio(lineA, divider[0])
    if r1 == -1:
        r2 = div_ratio(lineB, divider[0])  # div[0] lies on lineB
        if r2 == -1: return False
        r1 = div_ratio(lineA, divider[1])  # div[1] lies on lineA
        if r1 == -1: return False
    else:
        r2 = div_ratio(lineB, divider[1])
        if r2 == -1: return False
    
    # For everything else
    return True


def CF14C():
    N = int(input())
    result = []
    for _ in range(N):
        lines = []
        for _ in range(3):
            a, b, c, d = map(int, input().split())
            lines.append(((a, b), (c, d)))
        res = isA(lines)
        result.append("YES" if res else "NO")
    return result


res = CF14C()
print("\n".join(res))
