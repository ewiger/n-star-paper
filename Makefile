all: paper

clean:
		rm -f paper.aux \
			paper-blx.bib \
			paper.aux \
			paper.bbl \
			paper.blg \
			paper.log \
			paper.out \
			paper.pdf \
			paper.run.xml \
			paper.fls \
			paper.fdb_latexmk

paper: clean
		lualatex paper && bibtex paper && lualatex paper	
