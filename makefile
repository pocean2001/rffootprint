
all: 
	python stripline.py > stripline.kicad_mod
	python invertedf.py > invertedf.kicad_mod
	python patch.py > patch.kicad_mod

zip:
	zip -m -FS noname noname.drl noname*.g*

clean:
	rm -f *.pro *.kicad_mod *.drl *.g* *.dxf

.PHONY: all zip

