#!/usr/bin/env python
# encoding: utf-8
"""
regep.py

Created by Stephen Holiday on 2011-08-05.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
import os
import re
from optparse import OptionParser

def main():
    usage = "usage: %prog [options] RegExp"
    parser = OptionParser(usage)
    parser.add_option("-l", "--list",
                      action="store_true", dest="show_list",
                      help="Output as a python list")

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        parser.error("incorrect number of arguments")
        
    
    regep(options.show_list,args)
    exit()
        
def regep(show_list,args):
    try:
        try:
            regex=re.compile(args[0])
        except:
            print 'Regexp is invalid'
            exit()
        line=""
        while 1:
            next = sys.stdin.read(1)            # read a one-character string
            if not next:                        # or an empty string at EOF
                break
        
            if next=='\n':
                match=regex.search(line)
            
                if match is not None:
                    if show_list:
                        print list(match.groups())
                    else:
                        print '\t'.join(match.groups())
                else:
                    pass
                line=''
            else:
                line="%s%s"%(line,next)
                
                
    except KeyboardInterrupt:
        return
        
if __name__ == "__main__":
    main()
