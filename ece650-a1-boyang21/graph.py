from util import *
from intersect import *

# graph
class vertex(object):
    def __init__(self, pt, id):
        self.point = pt
        self.id = id

    def __repr__(self):
        return str(self.id) + ':  (' + pp(self.point.x) + ',' + pp(self.point.y) + ')'
        
    def __eq__(self, vt):
        return self.point  == vt.point 

class edge(object):
    def __init__(self, vt1, vt2):
        self.src = vt1
        self.dst = vt2

    def __repr__(self):
        return '<' + str(self.src.id) + ',' + str(self.dst.id) + '>'
        
    def __eq__(self, e):
        return (self.src  == e.src and self.dst  == e.dst ) or \
               (self.src  == e.dst and self.dst  == e.src ) 
    
