def line_intersection(line1, line2):
    xdiff = (x1 - x2, x3 - x4)
    ydiff = (y1 - y2, y3 - y4) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det((x1, y1), (x2, y2)), det((x3, y3), (x4, y4)))
    x = det(d, xdiff) * 1.0 / div
    y = det(d, ydiff) * 1.0 / div
    return x, y

#line 1
A = [2, 2]
B = [3, 3]

#line 2
C = [1, 4]
D = [5, 4]
print line_intersection((A, B), (C, D))
