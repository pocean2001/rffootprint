
import sys
import svgwrite

class Footprint:

    def pos(self, pos, origin=(0, 0)):
        vx, vy = self.viewport
        k = 3.543307
        x = pos[0] + origin[0] - vx
        y = pos[1] + origin[1] - vy
        if self.flip: y = self.size[1] - y
        return (k * x, k * y)

    def __init__(self, **kw):
        self.initialize(**kw)

    ############

    def initialize(self, viewport=(0,0), size=(100,100), flip=False):
        self.dwg = svgwrite.Drawing(profile='tiny')
        self.flip = flip
        self.viewport = viewport
        self.dwg['width'] = size[0] * svgwrite.mm
        self.dwg['height'] = size[1] * svgwrite.mm

    def rect(self, size, origin=(0,0), **kw):
        w, h = size
        self.poly([(0, 0), (w, 0), (w, h), (0, h)], origin)

    def poly(self, points, origin=(0,0), **kw):
        points = map(lambda x: self.pos(x, origin), points)
        print(points)
        el = self.dwg.polygon(points)
        self.dwg.add(el)

    def write(self, filename=None, pretty=True):
        f = open(filename, "w") if filename else sys.stdout
        self.dwg.write(f, pretty=pretty)
        if filename: f.close()


