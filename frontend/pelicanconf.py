#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

from decouple import config

AUTHOR = "Ramjee Ganti"
SITENAME = "RS Group"
SITETITLE = "RS Group"
SITEURL = config("SITE_URL")

PATH = "content"

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"

COPYRIGHT_YEAR = datetime.today().year
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("The School of AI", "https://theschoolof.ai/"),)

# Social widget
SOCIAL = (("Github", "https://github.com/EVA4-RS-Group/Phase2"),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/Users/projects/work/learning/Phase2/frontend/themes/phantom"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican_javascript"]
