#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Sequence example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {"view": "Terminal", "value": "B"},
                {"view": "Terminal", "value": "C"},
                {"view": "Terminal", "value": "D"}
            ],
            "name": "Sequence BCD",
            "view": "Sequence"
        },
        {"view": "Terminal", "value": "E"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = to_png(data, path)
    print result[0][1].encode('utf-8')
