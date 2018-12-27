
from svgwrite import Drawing, mm
import time

class Footprint:

    def pos(self, pos, origin=(0, 0), flip=False):
        x = pos[0] + origin[0]
        y = pos[1] + origin[1]
        if not flip: y = self.board[1] - y
        return ((x - self.center[0]) * mm, (y - self.center[1]) * mm)

    def __init__(self, center=None, board=None, name=None):
        self.initialize(center=center, board=board, name=name)

    ############

    def initialize(self, center=None, board=None, name=None):
        name = name or 'noname'
        center = center or (0, 0)
        board = board or (0, 0)
        self.dwg = Drawing(name + '.svg')
        self.name = name
        self.center = center
        self.border = board

    def line(self, start, end, origin, width=None, layer=None, flip=False):
        self.dwg.add(self.dwg.line(
            start=self.pos(start, origin, flip=flip),
            end=self.pos(end, origin, flip=flip)))

    def rect(self, size, origin=(0,0), layer='F.Cu', flip=False):
        w, h = size
        self.dwg.add(self.dwg.rect(
            insert=self.pos(origin, flip=flip),
            size=(w * mm, h * mm)))

    def poly(self, points, origin=(0,0), layer='F.Cu', flip=False):
        points = map(lambda x: self.pos(x, origin, flip=flip), points)
        self.dwg.add(self.dwg.polygon(points))

    def edge(self, size, origin=(0,0), layer='Edge.Cuts', width=0.15, flip=False):
        points = [(0, 0), (w, 0), (w, h), (0, h), (0, 0)]
        points = map(lambda x: self.pos(x, origin, flip=flip), points)
        self.dwg.add(self.dwg.polyline(points))

    def via(self, point, origin=None, size=None, drill=None, pad=None, flip=None):
        pass

    def write(self):
        self.dwg.save(pretty=True)



def build(fp):
    # BLE Antenna Design Guide, NXP Semiconductors, p15
    board = (0, 32)
    center = (board[0] / 2, board[1] / 2)
    fp.initialize(center=center, board=board)
    fp.rect((-4.4, 1), origin=(4.4, 3), flip=True)
    fp.rect((-4.4, 1), origin=(4.4, 3 + 1 + 5.4), flip=True)
    fp.rect((1, 1 + 5.4 + 1 + 18.2), origin=(4.4, 3), flip=True)
    fp.write()

build(Footprint())



# layer = svg.layer(label="Cu")
# svg.add(layer)
# layer.add(svg.rect(50, 2, origin=(24, 0)))
# stroke = svg.stroke([(50, 0), (400, 0), (400,500), (50,500)])
# layer.add(stroke)

# edge cuts
# layer = svg.layer(label="Edge.Cuts")
# svg.add(layer)
# layer.add(svg.rec(0, ))

# stroke = svg.fill([(0, 0), (200, 0), (200,100), (0,100)], origin=(100,100))
# layer.add(stroke)

# fill = svg.fill([(0, 0), (200, 0), (200,100), (0,100)], origin=(100,300))
# layer.add(fill)


