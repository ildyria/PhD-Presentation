LATEXMK = latexmk -pdf
LATEX = pdflatex
READ = evince
SOURCES := $(wildcard Gimli*.tex) $(wildcard main.tex)
TIKZ := $(wildcard tikz/*.tex)
PDFS := $(notdir $(SOURCES:.tex=.pdf))
PNGS := $(notdir $(SOURCES:.tex=.png))
STY := $(wildcard *.sty)
IMG := $(wildcard graphics/*)

all: $(PDFS)

cleanpdf:
	@rm png/*.png 2> /dev/null || true
	@rm *.pdf 2> /dev/null || true

force: cleanpdf $(PDFS)

Gimli-at-CHES-17-09-27.pdf: Gimli-at-CHES-17-09-27.tex asm.tex bijectivity.tex $(TIKZ) setup.sty macros.tex
	@echo Gimli-at-CHES-17-09-27.tex
	$(LATEXMK) Gimli-at-CHES-17-09-27.tex

main.pdf: main.tex $(STY) $(IMG)
	$(LATEXMK) main.tex


open:
	${READ} $(PDFS)


clean:
	@echo cleaning...
	@rm *.aux 2> /dev/null || true
	@rm *.log 2> /dev/null || true
	@rm *.out 2> /dev/null || true
	@rm *.toc 2> /dev/null || true
	@rm *.snm 2> /dev/null || true
	@rm *.nav 2> /dev/null || true
	@rm *.vrb 2> /dev/null || true
	@rm *.bbl 2> /dev/null || true
	@rm *.blg 2> /dev/null || true
	@rm *.idx 2> /dev/null || true
	@rm *.lol 2> /dev/null || true
	@rm *.fls 2> /dev/null || true
	@rm *.nav 2> /dev/null || true
	@rm *.bcf 2> /dev/null || true
	@rm *.run.xml 2> /dev/null || true
	@rm *.fdb_latexmk 2> /dev/null || true

png: $(PDFS) $(PNGS)

%.png: %.pdf
	convert -density 300 $*.pdf -quality 90 $*.png
