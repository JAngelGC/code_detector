#13B - Letter A
import math
r = lambda: map(int,input().split())
#Function to check if the lines cross
def cross(a, b):
  return a[0] * b[1] - a[1] * b[0]
def dot(a, b):
  return a[0] * b[0] + a[1] * b[1]
# def l(v):
#   return math.hypot(*v)
def on_line(a, b):
  return dot(a, b) > 0 and cross(a, b) == 0 and abs(b[0]) <= abs(5 * a[0]) <= abs(4 * b[0]) and abs(b[1]) <= abs(5 * a[1]) <= abs(4 * b[1])
def is_A(a, b, c):
  a, b = set(a), set(b)
  if len(a & b) != 1:
    return False
  p1, = a & b
  p2, p3 = a ^ b
  v1 = (p2[0] - p1[0], p2[1] - p1[1])
  v2 = (p3[0] - p1[0], p3[1] - p1[1])
  if dot(v1, v2) < 0 or abs(cross(v1, v2)) == 0:
    return False
  v3 = (c[0][0] - p1[0], c[0][1] - p1[1])
  v4 = (c[1][0] - p1[0], c[1][1] - p1[1])
  return (on_line(v3, v1) and on_line(v4, v2)) or (on_line(v3, v2) and on_line(v4, v1))
for i in range(int(input())):
  xa1, ya1, xa2, ya2 = r()
  xb1, yb1, xb2, yb2 = r()
  xc1, yc1, xc2, yc2 = r()
  a, b, c = [(xa1, ya1), (xa2, ya2)], [(xb1, yb1), (xb2, yb2)], [(xc1, yc1), (xc2, yc2)]
  print ("YES" if is_A(a, b, c) or is_A(a, c, b) or is_A(b, c, a) else "NO")