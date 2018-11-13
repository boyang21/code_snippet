from intersect import *

class DBException(Exception):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

# street database
class street_db(object):
    def __init__(self):
        self._db = dict()
        
    def add(self, street_name, coords):
        if not street_name in self._db.keys():
            self._db[street_name] = dict()
        else: 
            raise DBException("add a street that is already in the database, use 'c' instead.")
        self._db[street_name]['name'] = street_name
        self._db[street_name]['segs'] = []
        for i in range(len(coords)-1):            
            seg = line( point(coords[i][0], coords[i][1]), 
                        point(coords[i+1][0], coords[i+1][1]))
            self._db[street_name]['segs'].append(seg)
                        
        
    def chg(self, street_name, coords):
        if street_name in self._db.keys():
            self._db[street_name]['segs'] = [] 
        else:
            raise DBException("change a street that doesn't exist.")


        for i in range(len(coords)-1):            
            seg = line( point(coords[i][0], coords[i][1]), 
                        point(coords[i+1][0], coords[i+1][1]))
            self._db[street_name]['segs'].append(seg)


    def rm(self, street_name):
        if street_name in self._db.keys():
            self._db.pop(street_name)
        else:
            raise DBException("remove a street that doesn't exist.")


    def get_names(self):
        return self._db.keys()
        

    def get_segs(self, street_name):
        return self._db[street_name]['segs']
        



