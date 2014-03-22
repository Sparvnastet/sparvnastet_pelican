# coding: utf-8

import os
# Base settings that are common to production and development versions.
# Override these settings in ``local.py`` for local development.

SSH_HOST = 'host.example.com'
SSH_USER = 'ssh-user'
SSH_PASSWORD = 'the-secret-password'
SSH_PORT = '22'

SITE_ROOT = '/var/sparvnastet_pelican/sparvnastet_pelican/'

BASEDIR = os.path.dirname(os.path.abspath(os.path.join(__file__, '../')))
INPUTDIR = os.path.join(BASEDIR, 'content')
OUTPUTDIR = os.path.join(BASEDIR, "output")

CALENDAR_OUTPUT_DIR = OUTPUTDIR
CALENDAR_INPUT_DIR = os.path.join(INPUTDIR, "calendar")
