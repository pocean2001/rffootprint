
import time

class Footprint:

    def pos(self, pos, origin, flip=False):
        cx, cy = self.center
        x = pos[0] + origin[0]
        y = pos[1] + origin[1]
        if flip: y = self.board[1] - y
        return x - cx, y - cy

    def line(self, start, end, origin, width=None, layer=None, flip=False):
        self.state += "(fp_line\n"
        self.state += "  (start %g %g)\n" % self.pos(start, origin, flip=flip)
        self.state += "  (end %g %g)\n" % self.pos(end, origin, flip=flip)
        self.state += "  (layer {layer}) (width {width}))\n".format(
                      layer=layer, width=width)

    def initialize(self, name=None, center=None, board=None):
        self.center = center or (0, 0)
        self.board = board or (0, 0)
        name = name or 'name'
        unit = "R"   # prefix for the part
        tedit = int(round(time.time()))
        self.state = """\
(module {name} (layer F.Cu) (tedit {tedit:8X})
  (fp_text reference {unit}** (at 0 0.5) (layer F.SilkS) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value {name} (at 0 -0.5) (layer F.Fab) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
""".format(tedit=tedit, name=name, unit=unit)

    ############

    def __init__(self, name=None, center=None, board=None):
        self.initialize(name=name, center=center, board=board)

    def poly(self, points, origin=(0,0), layer='F.Cu', flip=False):
        self.state += "(fp_poly (pts\n"
        for p in points + points[:1]:
            self.state += "  (xy %g %g)\n" % self.pos(p, origin, flip=flip)
        self.state += "  ) (layer {layer}) (width 0))\n".format(layer=layer)

    def rect(self, size, origin=(0,0), layer='F.Cu', flip=False):
        w, h = size
        points = [(0, 0), (w, 0), (w, h), (0, h)]
        self.poly(points, origin=origin, layer=layer, flip=flip)

    def via(self, point, origin=(0,0), size=(1,1), drill=0.5, pad=1, flip=False):
        self.state += "(pad {pad} thru_hole circle\n".format(pad=pad)
        self.state += "  (at %d %d)\n" % self.pos(point, origin, flip=flip)
        self.state += "  (size {sizex:g} {sizey:g})\n".format(sizex=size[0], sizey=size[1])
        self.state += "  (drill {drill:g}) (layers *.Cu))\n".format(drill=drill)

    def edge(self, size, origin=(0,0), width=0.15, layer='Edge.Cuts', flip=False):
        w, h = size
        start = (0, 0)
        for end in [(w, 0), (w, h), (0, h), (0, 0)]:
           self.line(start, end, origin=origin, width=width, layer=layer, flip=flip)
           start = end

    def write(self):
        print(self.state + ")")


