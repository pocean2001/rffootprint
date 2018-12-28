# d = ' L '.join(map(lambda x: "%.5f %.5f" % x, points))
# self.add(self.dwg.path(d='M ' + d + ' z'))
# in inkscape, path > union, then opitonally path > stroke to path

import svgwrite
import sys

class Footprint:

    def pos(self, pos, origin=(0, 0)):
        k = 3.543307
        x = pos[0] + origin[0]
        y = pos[1] + origin[1]
        return (k * x, k * y)

    def __init__(self, **kw):
        self.initialize()

    ############

    def initialize(self, **kw):
        self.dwg = svgwrite.Drawing(profile='tiny')

    def line(self, start, end, origin, **kw):
        start = self.pos(start, origin)
        end = self.pos(end, origin)
        el = self.dwg.line(start, end)
        self.dwg.add(el)

    def rect(self, size, origin=(0,0), **kw):
        w, h = size
        self.poly([(0, 0), (w, 0), (w, h), (0, h)], origin)

    def poly(self, points, origin=(0,0), **kw):
        points = map(lambda x: self.pos(x, origin), points)
        el = self.dwg.polygon(points)
        self.dwg.add(el)

    def edge(self, size, origin=(0,0), **kw):
        self.dwg['width'] = size[0] * svgwrite.mm
        self.dwg['height'] = size[1] * svgwrite.mm

    def via(self, point, **kw):
        pass

    def write(self, filename=None, pretty=True):
        f = open(filename, "w") if filename else sys.stdout
        self.dwg.write(f, pretty=pretty)
        if filename: f.close()


if __name__ == '__main__':
    fp = Footprint()
    fp.rect((-4.4, 1), origin=(4.4, 3))
    fp.rect((-4.4, 1), origin=(4.4, 3 + 1 + 5.4))
    fp.rect((1, 1 + 5.4 + 1 + 18.2), origin=(4.4, 3))
    fp.edge((16, 32))
    fp.write('noname.svg')



