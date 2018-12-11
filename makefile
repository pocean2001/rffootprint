
all: 
	python invertedf.py > invertedf.kicad_mod
	python patch.py > patch.kicad_mod

clean:
	rm -f *.kicad_mod

.PHONY: all clean

