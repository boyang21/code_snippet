#!/usr/bin/python

import sys

from cmd_parser import *
from street_db import *
from graph_gen import *

def coords_str2tuple(coords_str):
    tuple_re = re.compile("\((-?\d+),\s*(-?\d+)\)")
    ini_flag = True
    for match in tuple_re.finditer(coords_str):
       if ini_flag:
           result = ((int(match.group(1)), int(match.group(2))), )
           ini_flag = False
       else:
           result += ((int(match.group(1)), int(match.group(2))), )
    return result    

def main():
    ### YOUR MAIN CODE GOES HERE

    db = street_db()
    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        action = None
        try:
            action, street_name, coords = cmd_parser(line.strip('\n'))
            if coords:
                coords = coords_str2tuple(coords)            
        except ParseException as ex:
            sys.stderr.write("Error: {0}\n".format(ex))

        if action == 'a':
            try:
                db.add(street_name, coords)
            except DBException as ex:
                sys.stderr.write("Error: {0}\n".format(ex))
        if action == 'c':
            try:
                db.chg(street_name, coords)
            except DBException as ex:
                sys.stderr.write("Error: {0}\n".format(ex))
        if action == 'r':
            try:
                db.rm(street_name)
            except DBException as ex:
                sys.stderr.write("Error: {0}\n".format(ex))
        if action == 'g':
            graph_gen(db)
        

    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()
