#!/usr/bin/env python
import plumage

SITENAME = "Adrin's Blog"
SITEURL = ""
AUTHOR = "adrin"

PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social links (Plumage uses these in the sidebar)
SOCIAL = (
    ("email", "mailto:adrin.jalali@gmail.com"),
    ("github", "https://github.com/adrinjalali"),
    ("stack-overflow", "https://stackoverflow.com/users/2536294/adrin"),
    ("linkedin", "https://de.linkedin.com/in/adrinjalali"),
)

# Menu items (displayed before pages in navigation)
MENUITEMS = (
    ("Blog", "/"),
    ("Search", "/pages/search.html"),
)

# Sidebar links (social is separate)
LINKS = ()

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Static files (includes custom CSS and JS)
STATIC_PATHS = ["files", "images", "static"]

# Favicon files - copy to root
EXTRA_PATH_METADATA = {
    "files/favicon.ico": {"path": "favicon.ico"},
    "files/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "files/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "files/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "files/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "files/favicon.png": {"path": "favicon.png"},
}

# Disable Plumage's auto-generated favicons
FAVICONS = False
OUTPUT_RETENTION = [".git"]

# Theme
THEME = plumage.get_path()
THEME_TEMPLATES_OVERRIDES = ["templates"]
TYPOGRIFY = True

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins (namespace plugins auto-discovered, just list them)
PLUGINS = ["sitemap", "webassets"]

# Sitemap
SITEMAP = {"format": "xml"}

# Markdown settings
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": True},
    },
    "output_format": "html5",
}

# Disable MyST reader (Plumage includes it, but we use standard Pelican markdown)
# MyST reader tries to parse .md files, we want the standard MarkdownReader
from pelican.readers import MarkdownReader
READERS = {"md": MarkdownReader}

# Disable unused outputs (also hides "Browse content by" in footer)
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
USE_FOLDER_AS_CATEGORY = False

# License (displayed in footer by Plumage)
LICENSE = "CC-BY-SA-4.0"
