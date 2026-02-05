# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal blog/website built with [Pelican](https://getpelican.com/), a static site generator written in Python. The site is published to GitHub Pages.

## Common Commands

```bash
# Install dependencies
pip install pelican typogrify Markdown bs4 ghp-import

# Update submodules (themes and plugins)
git submodule update --recursive --remote

# Generate site (development)
make html

# Serve locally with auto-regeneration
make devserver              # default port 8000
make devserver PORT=8080    # custom port

# Generate for production
make publish

# Deploy to GitHub Pages (generates and pushes to master branch)
make github

# Clean generated output
make clean
```

## Project Structure

- `content/` - Source content
  - `blog/` - Blog posts as Markdown files (named `YYYYMMDD-slug.md`)
  - `pages/` - Static pages (home, CV, contact)
  - `files/` - Static files (PDFs, images)
- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration (extends pelicanconf.py)
- `pelican-themes/` - Git submodule containing theme (uses `pelican-elegant`)
- `pelican-plugins/` - Git submodule containing plugins (uses `sitemap`, `extract_toc`, `tipue_search`)
- `output/` - Generated static site (not committed on `source` branch)

## Branch Structure

- `source` - Main development branch containing Pelican source
- `master` - GitHub Pages deployment branch (generated HTML)

## Content Format

Blog posts use Pelican's Markdown format with metadata headers. Static files go in `content/files/` and are referenced via `/files/` paths.
