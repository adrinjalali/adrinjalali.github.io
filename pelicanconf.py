#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'adrin'
SITENAME = 'Adrin Jalali'
SITE_DESCRIPTION="Anyone who knows anything of history knows that great social changes are impossible without feminine upheaval. Social progress can be measured exactly by the social position of the fair sex, the ugly ones included -- Karl Marx"
SITEURL = 'http://adrin.info'
#SITEURL = 'file:///.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN=SITEURL
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('email', 'mailto:adrin.jalali@gmail.com'),
          ('github', 'https://github.com/adrinjalali'),
          ('stack-overflow', 'http://stackoverflow.com/users/2536294/adrin'),
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

THEME="pelican-themes/pelican-elegant"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
DISQUS_SITENAME = u'adrin'
DISQUS_SITEURL= u'adrin.info'
DISQUS_SHORTNAME='adrin'
RECENT_ARTICLES_COUNT=5
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
SITE_LICENSE='<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'

MAILCHIMP_FORM_ACTION=True

SITEMAP={'format':'xml'}
