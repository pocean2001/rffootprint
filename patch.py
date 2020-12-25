# 2.4GHz Patch

from footprint import Footprint

def build(fp):

    board = fp.board
    corner = (-board[0]/2, -board[1]/2)

    # add border to all layers
    fp.edge(board, origin=corner, layer='Edge.Cuts')
    fp.edge(board, origin=corner, layer='F.Mask')
    fp.edge(board, origin=corner, layer='B.Mask')
    fp.edge(board, origin=corner, layer='F.Cu')
    fp.edge(board, origin=corner, layer='B.Cu')

    # ground plane on back
    fp.rect(board, origin=corner, layer='B.Cu')

    # solder mask for SMA edge connector
    fp.rect((8, -4), origin=(-4, board[1]/2), layer='F.Mask')
    fp.rect((8, -4), origin=(-4, board[1]/2), layer='B.Mask')

    # patch
    l = 27.2   # length of patch
    w = 50.8   # width of patch
    fp.rect((w, l), origin=(-w/2, -l/2))

    # hi-Z quarter wave line
    h = 1.58   # dieletric (Er=4.2) height, ie 1/16"
    dl = 18    # length of quarter wave line
    dw = 1.3   # width of quarter wave line
    zw = 3.1   # width of 50 ohm line
    lh = .44   # open-circuit extension (l/h) of the 50 ohm line (from Puff book p37)
    lsh = lh * (1 - dw / zw)  
    ext = h * lsh
    dl += ext
    fp.rect((dw, dl), origin=(-dw/2, l/2))

    # 50 ohm line
    d = l/2 + dl
    zl = board[1]/2 - d
    fp.rect((zw, zl), origin=(-zw/2, d))
    fp.write()


build(Footprint(board=(100, 80)))


