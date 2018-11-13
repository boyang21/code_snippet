from util import *

def pp(x):
    """Returns a pretty-print string representation of a number.
       A float number is represented by an integer, if it is whole,
       and up to two decimal places if it isn't
    """
    if isinstance(x, float):
        if x.is_integer():
            return str(int(x))
        else:
            return "{0:.2f}".format(x)
    return str(x)

class point(object):
    """A point in a two dimensional space"""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __repr__(self):
        return '(' + pp(self.x) + ', ' + pp(self.y) + ')'
        
    def __eq__(self, pt):
        return self.x == pt.x and self.y == pt.y

    def hash(self):
        return (self.x, self.y)

class line(object):
    """A line between two points"""
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return '['+ str(self.src) + '-->' + str(self.dst) + ']'

    def __eq__(self, ln):
        return (self.src == ln.src and self.dst == ln.dst) or \
               (self.src == ln.dst and self.dst == ln.src)

def intersect (l1, l2):
    """Returns a point at which two lines intersect"""
    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y

    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y
    
    xdiff = (x1 - x2, x3 - x4)
    ydiff = (y1 - y2, y3 - y4) 

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    # parallel case
    if div == 0:
        # check overlap
        if x1 < x2:
            l1_l_x = x1
            l1_l_y = y1
            l1_r_x = x2
            l1_r_y = y2
        if x1 > x2:
            l1_l_x = x2
            l1_l_y = y2
            l1_r_x = x1
            l1_r_y = y1
        if x1 == x2:
            if y1 < y2:
                l1_l_x = x1
                l1_l_y = y1
                l1_r_x = x2
                l1_r_y = y2
            else:                
                l1_l_x = x2
                l1_l_y = y2
                l1_r_x = x1
                l1_r_y = y1            
        if x3 < x4:
            l2_l_x = x3
            l2_l_y = y3
            l2_r_x = x4
            l2_r_y = y4
        if x3 > x4:
            l2_l_x = x4
            l2_l_y = y4
            l2_r_x = x3
            l2_r_y = y3
        if x3 == x4:
            if y3 < y4:
                l2_l_x = x3
                l2_l_y = y3
                l2_r_x = x4
                l2_r_y = y4
            else:                
                l2_l_x = x4
                l2_l_y = y4
                l2_r_x = x3
                l2_r_y = y3            
            
        xcoor1 = max(l1_l_x, l2_l_x)
        ycoor1 = max(l1_l_y, l2_l_y)
        xcoor2 = min(l1_r_x, l2_r_x)
        ycoor2 = min(l1_r_y, l2_r_y)        

        result = []
        # condition1: on the same line
        # condition2: (xcoor, ycoor) on both lines
        if (y1-y2) * (x1-x3) == (y1-y3) * (x1-x2):
            if xcoor1 >= l1_l_x and xcoor1 <= l1_r_x and \
               xcoor1 >= l2_l_x and xcoor1 <= l2_r_x and \
               ycoor1 >= l1_l_y and ycoor1 <= l1_r_y and \
               ycoor1 >= l2_l_y and ycoor1 <= l2_r_y:
                result.append( point(xcoor1, ycoor1) )
            if xcoor2 >= l1_l_x and xcoor2 <= l1_r_x and \
               xcoor2 >= l2_l_x and xcoor2 <= l2_r_x and \
               ycoor2 >= l1_l_y and ycoor2 <= l1_r_y and \
               ycoor2 >= l2_l_y and ycoor2 <= l2_r_y:
                result.append( point(xcoor2, ycoor2) )
        return result

    d = (det((x1, y1), (x2, y2)), det((x3, y3), (x4, y4)))
    xcoor = det(d, xdiff) * 1.0 / div
    ycoor = det(d, ydiff) * 1.0 / div
    

    if xcoor >= min(x1, x2) and xcoor <= max(x1, x2) and \
       ycoor >= min(y1, y2) and ycoor <= max(y1, y2) and \
       xcoor >= min(x3, x4) and xcoor <= max(x3, x4) and \
       ycoor >= min(y3, y4) and ycoor <= max(y3, y4):
        return [point(xcoor, ycoor)]
    else:
        return []


if __name__ == '__main__':
    pass
