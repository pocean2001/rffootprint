
all:
	python3 footprintsvg.py

examples: 
	python3 invertedf.py > invertedf.kicad_mod
	python3 patch.py > patch.kicad_mod
	python3 invertedf_poly.py > invertedf_poly.kicad_mod

zip:
	sh zip.sh

clean:
	rm -f *.kicad_mod

.PHONY: all clean

