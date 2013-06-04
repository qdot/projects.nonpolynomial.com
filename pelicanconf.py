#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Machulis'
SITENAME = u'Nonpolynomial Labs Portfolio'
SITEURL = 'http://projects.nonpolynomial.com'

TIMEZONE = 'US/Pacific'

MARKUP = (('md', 'markdown', 'html'))

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED = None

THEME = "themes/nonpolynomial-portfolio"

# Relative to content dir
ARTICLE_DIR = 'projects'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_SAVE_AS = None
CATEGORY_SAVE_AS = None
TAG_SAVE_AS = None
AUTHOR_SAVE_AS = None

DAY_ARCHIVE_SAVE_AS = None
MONTH_ARCHIVE_SAVE_AS = None
YEAR_ARCHIVE_SAVE_AS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TEMPLATE_PAGES = {'templates/404.html': "404/index.html"}

FILES_TO_COPY = [('extras/htaccess', '.htaccess')]

DIRECT_TEMPLATES = ['index']

MD_EXTENSIONS = ['codehilite', 'extra', 'video']
