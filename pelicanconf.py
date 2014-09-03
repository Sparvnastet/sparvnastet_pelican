#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

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
LINKS = (
    ('Forskningsavdelningen', 'http://forskningsavd.se/'),
    ('Göteborgs Hackerspace', 'http://gbg.hackerspace.se/'),
    ('Umeå Hackerspace', 'http://umeahackerspace.se/'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sparvnastet'),
          ('github', 'https://github.com/sparvnastet'),)


DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'files',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }

PLUGINS = [
    'pelican_vimeo',
    'pelican_youtube',
]


