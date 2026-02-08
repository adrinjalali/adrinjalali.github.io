.PHONY: help clean html serve build publish

PELICAN=uv run pelican
INPUTDIR=content
OUTPUTDIR=output
CONFFILE=pelicanconf.py
PUBLISHCONF=publishconf.py

help:
	@echo 'Makefile for adrin.info'
	@echo ''
	@echo 'Usage:'
	@echo '   make html        Generate site for development'
	@echo '   make serve       Serve site locally with auto-reload'
	@echo '   make build       Full production build (pelican + pagefind)'
	@echo '   make publish     Alias for build'
	@echo '   make clean       Remove generated files'

clean:
	rm -rf $(OUTPUTDIR)

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)
	cp $(INPUTDIR)/files/favicon.ico $(OUTPUTDIR)/favicon.ico
	cp $(INPUTDIR)/files/favicon-*.png $(OUTPUTDIR)/
	cp $(INPUTDIR)/files/apple-touch-icon.png $(OUTPUTDIR)/

serve:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

build: clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)
	cp $(INPUTDIR)/files/favicon.ico $(OUTPUTDIR)/favicon.ico
	cp $(INPUTDIR)/files/favicon-*.png $(OUTPUTDIR)/
	cp $(INPUTDIR)/files/apple-touch-icon.png $(OUTPUTDIR)/
	npx pagefind --site $(OUTPUTDIR)

publish: build
