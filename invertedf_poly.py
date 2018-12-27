
"""
         | --
         |  |
         |  |
         |  18.2mm
         |  |
         |  |
4.4mm    | _|
=========| __
         |  |
         |  5.4mm 
         | _|
=========|
        1mm
"""

from footprint import Footprint

def build(fp):
    w = 4.4
    h = 1 + 5.4 + 1 + 18.2
    fp.poly([(0, 0), (w + 1, 0), (w + 1, h),
             (w, h), 
             (w, 2 + 5.4), 
             (0, 2 + 5.4),
             (0, 1 + 5.4),
             (w, 1 + 5.4),
             (w, 1),
             (0, 1)], flip=True)
    fp.write()

build(Footprint())

