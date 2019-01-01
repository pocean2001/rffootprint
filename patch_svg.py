
import sys
from footprintsvg import Footprint

bh = 100        # 103
bw = 80         # 78
er = 4.2        # loss tangent is .017
h = 1.6         # height of the board
w, l = 30, 27.5 # length and width of patch
zw = 3.1        # width of 50 ohm line
de = 0.5        # offset from edge

# simple calculations
cx = bw / 2
cy = bh / 2

# board
fp = Footprint(size=(bw, bh), viewport=(-cx, -cy), rotate=True)

# 50 ohm line
d0 = cy - 20 - l
fp.rect((w, l), origin=(-w/2, d0))
zl = -cy - d0
fp.rect((zw, zl), origin=(-zw/2, d0))

# stub match
line = 22.3  # 117 deg / 50 ohms
stub = 11    # 58 deg / 50 ohms
fp.rect((stub, zw), origin=(zw/2, d0 - line - zw/2))

fp.write("patch_svg.svg")






