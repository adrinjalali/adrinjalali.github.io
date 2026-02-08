#!/usr/bin/env python
# This file is only used for production builds (make publish)

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://adrin.info"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Include CNAME for GitHub Pages custom domain
# Note: inherits STATIC_PATHS from pelicanconf.py which includes "static"
