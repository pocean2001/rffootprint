# 2.4GHz Patch

l = 29.2   # length of patch
w = 50.8   # width of patch
dl = 18    # length of quarter wave line
dw = 1.3   # width of quarter wave line
zw = 3.1   # width of 50 ohm line
h = 1.58   # dieletric (Er=4.2) height, ie 1/16"
ext = .44  # open-circuit extension (l/h) of 50 ohm line

from footprint import Footprint

fp = Footprint()
board = (100, 80)
ext = h * .44 * (1 - dw / zw) 

fp.edge(board, origin=(-board[0]/2, -board[1]/2), layer='Edge.Cuts')
fp.rect(board, origin=(-board[0]/2, -board[1]/2), layer='B.Cu')
fp.rect((w, l), origin=(-w/2, -l/2))
fp.rect((dw, dl + ext), origin=(-dw/2, l/2))
d = l/2 + dl + ext 
fp.rect((zw, board[1]/2 - d), origin=(-zw/2, d))
fp.write()

