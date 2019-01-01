
## footprint

Create KiCad footprints using Python 3.

![](invertedf.png)

The library provides the following methods:

```
footprint.__init__(name='name', center=(0,0), board=(0,0))
   - 'board' sets the size of the board (used by 'flip')
   - 'center' sets the center point of the footprint
   - 'name' sets the name of the footprint

footprint.poly(points, origin=(0,0), layer='F.Cu', flip=False)
   - draw a filled polygon using the points listed in 'points'
   - 'origin' sets the starting corner of the rectangle
   - 'layer' sets the KiCad PCB layer 
   - setting 'flip' flips the Y axis

footprint.rect(size, origin=(0,0), layer='F.Cu', flip=False)
   - draw a filled rectangle using a polygon
   - 'origin' sets the starting corner of the rectangle
   - 'layer' sets the KiCad PCB layer 
   - setting 'flip' flips the Y axis

footprint.edge(size, origin=(0,0), width=0.15, layer='Edge.Cuts', flip=False)
   - draw a unfilled rectange using lines
   - 'origin' sets the starting corner of the rectangle
   - 'width' sets the width of the line along the rectangle
   - 'layer' sets the KiCad PCB layer 
   - setting 'flip' flips the Y axis

footprint.via(pos, origin=(0,0), size=(1,1), drill=0.5, pad=1, flip=False)
   - create a via at pos + origin
   - 'size' sets the size of the via
   - 'drill' sets the size of the drill hole
   - 'pad' sets the type of the via
   - setting 'flip' flips the Y axis

footprint.write()
   - print the KiCad footprint to stdout
```

For example, the following is a 2.4GHz BLE inverted F antenna.  The dimensions
were taken from the NXP Antenna Design Guide, page 15.

```
from footprint import Footprint
board = (0, 32)
center = (board[0]/2, board[1]/2)
fp = Footprint(center=center, board=board)
fp.rect((-4.4, 1), origin=(4.4, 3), flip=True)
fp.rect((-4.4, 1), origin=(4.4, 3 + 1 + 5.4), flip=True)
fp.rect((1, 1 + 5.4 + 1 + 18.2), origin=(4.4, 3), flip=True)
fp.write()
```
or

```
from footprint import Footprint
fp = Footprint()
w = 4.4
h = 1 + 5.4 + 1 + 18.2
fp.poly([(0, 0), (w + 1, 0), (w + 1, h), (w, h), 
         (w, 2 + 5.4), (0, 2 + 5.4), (0, 1 + 5.4),
         (w, 1 + 5.4), (w, 1), (0, 1)], flip=True)
fp.write()
```

![](invertedf.png)

Next is a 2.4GHz patch antenna created using
the patch16.exe DOS program by WB0DGF.  A full PCB
is created by the following code.  


```
# 2.4GHz Patch

l = 27.2   # length of patch
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
corner = (-board[0]/2, -board[1]/2)

fp.edge(board, origin=corner, layer='Edge.Cuts')
fp.rect(board, origin=corner, layer='B.Cu')

fp.rect((8, -4), origin=(-4, board[1]/2), layer='F.Mask')
fp.rect((8, -4), origin=(-4, board[1]/2), layer='B.Mask')

fp.rect((w, l), origin=(-w/2, -l/2))
fp.rect((dw, dl + ext), origin=(-dw/2, l/2))
d = l/2 + dl + ext 
fp.rect((zw, board[1]/2 - d), origin=(-zw/2, d))
fp.write()
```
![](patch.png)

The simpliest way
to import this PCB (or other footprints) into KiCad
is to first run Pcbnew, click open footprint
editor, in the editor click import footprint, and
lastly click insert footprint into current board.
Go back to Pcbnew and find the footprint at 0,0 in the 
upper left hand corner. 

The file 'patch.svg' was created by printing the F-Cu layer
only of the footprint in Pcbnew.  The result was then modified
in Inkscape: first changing the bounding box, removing
the fill from the rectangles and lastly unioning the result
to remove the line crossings.

![](patch.svg)

Cutting the SVG file (without the unioning) on copper foil tape with a vinyl cutter gave the following:

![](patch.jpg)

## footprintsvg

Like footprint but generates svg files for say an vinyl cutter.  See patch_svg.py.
It generates the following svg file:

![](patch_svg.svg)

