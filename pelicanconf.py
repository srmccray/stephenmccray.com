#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stephen McCray'
SITENAME = u'stephenmccray.com'
SITEURL = 'http://127.0.0.1:8000'

# paths
PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'

DIRECT_TEMPLATES = ['index', 'archives', 'tags', 'categories']
TEMPLATE_PAGES = {'templates/index.html': 'index.html', }

TIMEZONE = 'America/Vancouver'


DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/pelican-bootstrap3/"
BOOTSTRAP_THEME = 'slate'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_SUMMARY = True
SUMMARY_MAX_LENGTH = 25
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
