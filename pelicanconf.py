#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sparvn\xe4stet'
SITENAME = u'Sparvn\xe4stet'
SITEURL = ''

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = u'se'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'themes/sparrowtheme'
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sparvnastet'),
          ('github', 'https://github.com/sparvnastet'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', ]

PLUGINS = [
    'pelican_vimeo',
    'pelican_youtube',
]