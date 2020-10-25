#!/usr/bin/env python3

from itertools import groupby

def foo(S):
    groups = []
    for k, g in groupby(S):
        groups.append((k, list(g)))
    for (k,v) in groups:
        print('({}, {}) '.format(len(v), k), end='')

if __name__ == "__main__":
    foo(input())
            
    
