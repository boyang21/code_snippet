""" command parser """

import re

class ParseException(Exception):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)


def cmd_parser(line):
    if line.strip() == 'g':
        return 'g', None, None
    fmt = re.compile(r"^([acr])\s+\"([a-z\sA-Z]+)\"(.*)$")
    match = fmt.match(line)
    if match == None:
        raise ParseException("wrong command format.")
    else:
        if match.group(1) == 'r':
            return match.group(1), match.group(2), None
        else:
            fmt_coors = re.compile(r"^(\(\s*[-\d]\d*\s*,\s*[-\d]\d*\s*\)\s*){2,}(\s*)$")
            if not fmt_coors.match(match.group(3).strip()):
                raise ParseException("wrong command format for the coors part.")
            else:
                # action, streetname, coors
                return match.group(1), match.group(2), match.group(3).strip()
