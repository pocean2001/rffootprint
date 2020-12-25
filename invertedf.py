"""
       1mm _
         |  |
         |  |
         |  |
         |  18.2mm
         |  |
         |  |
         | _|
=========| __
         |  |
         |  5.4mm 
         | _|
=========|
h = 4.4mm
"""

from footprint import Footprint

def build(fp):
    # BLE Antenna Design Guide, NXP Semiconductors, p15
    fp.rect((-4.4, 1), origin=(4.4, 3))
    fp.rect((-4.4, 1), origin=(4.4, 3 + 1 + 5.4))
    fp.rect((1, 1 + 5.4 + 1 + 18.2), origin=(4.4, 3))
    fp.write()

board = (0, 32)
center = (board[0] / 2, board[1] / 2)
fp = Footprint(center=center, board=board, flip=True)
build(fp)


