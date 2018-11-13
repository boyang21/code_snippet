from intersect import *
from graph import *

def print_graph(vertices, edges):
    if vertices:
        print "V = {"
        print '\n'.join(['  ' + str(vt) for vt in vertices])
        print "}"
    else:
        print "V = {"
        print "}"        
    if edges:
        print "E = {"
        print ',\n'.join(['  ' + str(edg) for edg in edges])
        print "}"
    else:
        print "E = {"
        print "}"        

    
    
""" graph generator """
""" Returns a set of edges and a list of vertices """
def graph_gen(street_db):
    street_names = street_db.get_names()
    # graph database
    graph_db = dict()
    for st_name in street_names:
        graph_db[st_name] = []
        for seg in street_db.get_segs(st_name):
            graph_db[st_name].append( [] )
            

    for i1, st1_name in enumerate(street_names):
        for j1, seg1 in enumerate(street_db.get_segs(st1_name)):
            for st2_name in street_names[i1+1:]:
                for j2, seg2 in enumerate(street_db.get_segs(st2_name)):
                    intersect_pts = intersect(seg1, seg2)
                    # update graph db
                    if intersect_pts:
                        for intersect_pt in intersect_pts:
                            if not intersect_pt in graph_db[st1_name][j1]:
                                graph_db[st1_name][j1].append(intersect_pt)
                            if not seg1.src in graph_db[st1_name][j1]:
                                graph_db[st1_name][j1].append(seg1.src)
                            if not seg1.dst in graph_db[st1_name][j1]:
                                graph_db[st1_name][j1].append(seg1.dst)

                            if not intersect_pt in graph_db[st2_name][j2]:
                                graph_db[st2_name][j2].append(intersect_pt)
                            if not seg2.src in graph_db[st2_name][j2]:
                                graph_db[st2_name][j2].append(seg2.src)
                            if not seg2.dst in graph_db[st2_name][j2]:
                                graph_db[st2_name][j2].append(seg2.dst)
                    
                        
    # generate edges and vertices
    
    id = 0
    edges = []
    vertices = []
    # pt -> vertex
    pt_dict = dict()
    for st_name in street_names:
        for i, seg in enumerate(street_db.get_segs(st_name)):
            pt_lst = graph_db[st_name][i]
            if pt_lst: 
                # sort based on x axis first, then y axis
                pt_lst.sort(key=lambda pt: (pt.x, pt.y))

                for j in range( len(pt_lst) - 1 ):                    
                    pt1 = pt_lst[j]
                    pt2 = pt_lst[j+1]
                    v1 = vertex(pt1, id)
                    if not v1 in vertices:
                        vertices.append(v1)
                        pt_dict[pt1.hash()] = v1
                        id += 1
                    v2 = vertex(pt2, id)
                    if not v2 in vertices:
                        vertices.append(v2)
                        pt_dict[pt2.hash()] = v2
                        id += 1
                    if not pt1 == pt2:    
                        ed = edge(pt_dict[pt1.hash()], pt_dict[pt2.hash()])
                        if not ed in edges:
                            edges.append( ed )

    print_graph(vertices, edges)
    return 0


        
    
