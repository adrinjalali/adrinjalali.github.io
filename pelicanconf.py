#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'adrin'
SITENAME = 'Adrin Jalali'
SITEURL = 'http://adrin.info'
#SITEURL = 'file:///.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/adrinjalali'),
          ('stackoverflow', 'http://stackoverflow.com/users/2536294/adrin'),
          ('linkedin', 'de.linkedin.com/in/adrinjalali'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS=['files']
OUTPUT_RETENTION = (".git")
TYPOGRIFY=True
DISPLAY_PAGES_ON_MENU=False
MENUITEMS=(('Get in Touch', '/pages/get-in-touch'),
           ('Curriculum Vitae', '/pages/curriculum-vitae'),)

THEME="pelican-themes/pelican-bootstrap3"

PLUGIN_PATH = ['/home/adrin/html/pelican/pelican-plugins/']
#PLUGINS = [u'disqus_static']
DISQUS_SITENAME = u'adrin'
DISQUS_SITEURL= u'adrin.info'
DISQUS_SHORTNAME='adrin'
