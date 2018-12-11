
import time

class Footprint:

    def __init__(self, name='name', center=(0,0), board=(0,0)):
        tedit = int(round(time.time()))
        unit = "R"   # prefix for the part
        self.center = center
        self.board = board
        self.state = """\
(module {name} (layer F.Cu) (tedit {tedit:8X})
  (fp_text reference {unit}** (at 0 0.5) (layer F.SilkS) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value {name} (at 0 -0.5) (layer F.Fab) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
""".format(tedit=tedit, name=name, unit=unit)

    def write(self):
        print(self.state + ")")

    def rect(self, size, origin=(0,0), layer='F.Cu', flip=False):
        w, h = size
        x, y = origin
        if flip:
            h = -h
            y = self.board[1] - y
        center = self.center
        self.state += "(fp_poly (pts (xy %g %g)\n" % (x - center[0], y - center[1])
        self.state += "  (xy %g %g)\n" % (x + w - center[0], y - center[1])
        self.state += "  (xy %g %g)\n" % (x + w - center[0], y + h - center[1])
        self.state += "  (xy %g %g)\n" % (x - center[0], y + h - center[1])
        self.state += "  (xy %g %g))\n" % (x - center[0], y - center[1])
        self.state += "  (layer {layer}) (width 0))\n".format(
                      layer=layer)

    def line(self, size, origin=(0,0), width=0.15, layer=None):
        w, h = size
        x, y = origin
        center = self.center
        self.state += "(fp_line (start %g %g)\n" % (x - center[0], y - center[1])
        self.state += "  (end %g %g)\n" % (x + w - center[0], y + h - center[1])
        self.state += "  (layer {layer}) (width {width}))\n".format(
                      layer=layer, width=width)

    def edge(self, size, origin=(0,0), width=0.15, layer='Edge.Cuts'):
        w, h = size
        x, y = origin
        self.line((w, 0), (x, y), width=width, layer=layer)
        self.line((0, h), (x + w, y), width=width, layer=layer)
        self.line((-w, 0), (x + w, y + h), width=width, layer=layer)
        self.line((0, -h), (x, y + h), width=width, layer=layer)

    def via(self, pos, origin=(0,0), size=(1,1), drill=0.5, pad=1):
        w, h = pos
        x, y = origin
        center = self.center
        self.state += "(pad {pad} thru_hole circle\n".format(pad=pad)
        self.state += "  (at %d %d)\n" % (x + w - center[0], y + h - center[1])
        self.state += "  (size {sizex:g} {sizey:g})\n".format(sizex=size[0], sizey=size[1])
        self.state += "  (drill {drill:g}) (layers *.Cu))\n".format(drill=drill)

