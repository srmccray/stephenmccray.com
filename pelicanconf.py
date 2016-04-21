#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stephen McCray'
SITENAME = u'stephenmccray.com'
SITEURL = u'stephenmccray.com'

# paths
PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = ".\\pelican-themes\\simple-bootstrap"
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
SHOW_TAGS = True
DISPLAY_SUMMARY = True
SUMMARY_MAX_LENGTH = 25
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
