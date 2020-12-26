
import subprocess 

def run(command, language="", title=""):
    if title: title += "\n"
    proc = subprocess.Popen("PYTHONPATH=. " + command, shell=True, stdout=subprocess.PIPE)
    buf = proc.stdout.read().strip().decode()
    proc.wait()
    return f"""
```{language}
{title}{buf}
```
"""


print(f"""\
## footprint

Create KiCad footprints using Python 3.

![](invertedf.png)

The library provides the following methods:

```
footprint.__init__(name='name', center=(0,0), board=(0,0), flip=False)
   - 'board' sets the size of the board
   - 'center' sets the center point of the footprint
   - 'name' sets the name of the footprint
   - 'flip' if true flips board around y axis (y' = board[1] - y)

footprint.poly(points, origin=(0,0), layer='F.Cu')
   - draw a filled polygon using the points listed in 'points'
   - 'origin' sets the starting corner of the rectangle
   - 'layer' sets the KiCad PCB layer 

footprint.rect(size, origin=(0,0), layer='F.Cu')
   - draw a filled rectangle using a polygon
   - 'origin' sets the starting corner of the rectangle
   - 'layer' sets the KiCad PCB layer 

footprint.edge(size, origin=(0,0), width=0.15, layer='Edge.Cuts')
   - draw a unfilled rectange using lines
   - 'origin' sets the starting corner of the rectangle
   - 'width' sets the width of the line along the rectangle
   - 'layer' sets the KiCad PCB layer 

footprint.via(pos, origin=(0,0), size=(1,1), drill=0.5, pad=1)
   - create a via at pos + origin
   - 'size' sets the size of the via
   - 'drill' sets the size of the drill hole
   - 'pad' sets the type of the via

footprint.write()
   - print the KiCad footprint to stdout
```

For example, the following is a 2.4GHz BLE inverted F antenna.  The dimensions
were taken from the NXP Antenna Design Guide, page 15.

{run("cat invertedf.py", language="python")}

or

{run("cat invertedf_poly.py", language="python")}

![](invertedf.png)

Next is a 2.4GHz patch antenna created using
the patch16.exe DOS program by WB0DGF.  A full PCB
is created by the following code.  

{run("cat patch.py", language="python")}

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
(The cuts that cross the foil were the result of me forgetting to "union" the paths in inkscape before 
printing).

![](patch.jpg)


""")



