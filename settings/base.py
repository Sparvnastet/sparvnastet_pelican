# coding: utf-8

# Base settings that are common to production and development versions.
# Override these settings in ``local.py`` for local development.

SSH_HOST = 'host.example.com'
SSH_USER = 'ssh-user'
SSH_PASSWORD = 'the-secret-password'
SSH_PORT = '22'
HOST_SPARVNASTET = '%s@%s' % (SSH_USER, SSH_HOST)

SITE_ROOT = '/var/sparvnastet_pelican'