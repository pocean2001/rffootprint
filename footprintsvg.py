
import svgwrite
import sys

class Footprint:

    def tomm(self, pos):
        return (pos[0] * svgwrite.mm, pos[1] * svgwrite.mm)

    def pos(self, pos, origin=(0, 0), flip=False):
        cx, cy = self.center
        x = pos[0] + origin[0]
        y = pos[1] + origin[1]
        if not flip: y = self.board[1] - y
        return self.tomm((x - cx, y - cy))

    def add(self, el):
        self.dwg.add(el)
        # dwg = self.dwg
        # g = dwg.g()
        # g.add(el)
        # dwg.add(g)

    def __init__(self, center=None, board=None, **kw):
        self.initialize(center=center, board=board)

    ############

    def initialize(self, center=None, board=None, **kw):
        center = center or (0, 0)
        board = board or (0, 0)
        self.dwg = svgwrite.Drawing(profile='tiny')
        self.center = center
        self.border = board

    def line(self, start, end, origin, width=None, flip=False, **kw):
        start = self.pos(start, origin, flip=flip)
        end = self.pos(end, origin, flip=flip)
        self.add(self.dwg.line(start, end, stroke='black'))

    def rect(self, size, origin=(0,0), flip=False, **kw):
        insert = self.pos(origin, flip=flip)
        w, h = size
        points = [(0, 0), (w, 0), (w, h), (0, h)]
        self.add(self.poly(points, origin, flip=flip))
        # size = self.tomm(size)
        # self.add(self.dwg.rect(insert, size, fill='none', stroke='black'))

    def poly(self, points, origin=(0,0), flip=False, **kw):
        points = map(lambda x: self.pos(x, origin, flip=flip), points)
        self.add(self.dwg.polygon(points, stroke='black'))

    def edge(self, size, origin=(0,0), width=0.15, flip=False, **kw):
        size = self.tomm(size)
        self.dwg['width'] = size[0]
        self.dwg['height'] = size[1]
        # points = [(0, 0), (w, 0), (w, h), (0, h)]
        # points = map(lambda x: self.pos(x, origin, flip=flip), points)
        # self.dwg.add(self.dwg.polyline(points))

    def via(self, point, **kw):
        pass

    def write(self, filename=None, pretty=True):
        if filename:
            self.dwg.saveas(filename, pretty=pretty)
        else:
            self.dwg.write(sys.stdout, pretty=pretty)



def build(fp, filename=None):
    # BLE Antenna Design Guide, NXP Semiconductors, p15
    board = (16, 32)
    # center = (board[0] / 2, board[1] / 2)
    # fp.initialize(center=center, board=board)
    fp.initialize()
    fp.rect((-4.4, 1), origin=(4.4, 3), flip=True)
    fp.rect((-4.4, 1), origin=(4.4, 3 + 1 + 5.4), flip=True)
    fp.rect((1, 1 + 5.4 + 1 + 18.2), origin=(4.4, 3), flip=True)
    fp.edge(board)
    fp.write(filename)

build(Footprint())


