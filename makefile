
all: 
	python3 invertedf.py > invertedf.kicad_mod
	python3 patch.py > patch.kicad_mod

clean:
	rm -f *.kicad_mod

.PHONY: all clean

