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

def main():
    try:
        argv = sys.argv
        regex=re.compile(argv[1])
    
        line=""
        while 1:
            next = sys.stdin.read(1)            # read a one-character string
            if not next:                        # or an empty string at EOF
                break
        
            if next=='\n':
                match=regex.search(line)
            
                if match is not None:
                    print match.groups()
                else:
                    pass
                line=''
            else:
                line="%s%s"%(line,next)
                
                
    except KeyboardInterrupt:
        return
        
if __name__ == "__main__":
    main()
