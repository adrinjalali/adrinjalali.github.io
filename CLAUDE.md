# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal blog built with [Pelican](https://getpelican.com/) (Python static site generator), using the [Plumage](https://github.com/kdeldycke/plumage) theme and [Pagefind](https://pagefind.app/) for search.

## Commands

```bash
# Install dependencies
uv sync

# Development server with auto-reload
make serve

# Full production build (pelican + pagefind)
make build

# Generate without pagefind (faster for dev)
make html
```

## Deployment

Push to `source` branch triggers GitHub Actions (`.github/workflows/deploy.yml`) which builds and deploys to GitHub Pages.

## Project Structure

- `content/blog/` - Blog posts (Markdown, named `YYYYMMDD-slug.md`)
- `content/pages/` - Static pages
- `content/files/` - Static assets (PDFs, images)
- `pelicanconf.py` - Development config
- `publishconf.py` - Production config (extends pelicanconf)

## Content Format

Posts use Pelican's metadata format (not YAML front-matter):

```markdown
Title: My Post Title
Date: 2024-01-15
Tags: tag1, tag2
Category: category-name

Content starts here...
```

## Notes

- Theme (Plumage) and plugins are pip-installed, not vendored
- MyST reader is disabled in config (we use standard Pelican markdown)
- Search page at `/pages/search.html` uses Pagefind UI
