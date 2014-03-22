# coding: utf-8

# Import all the base settings
# and then let the local settings override those if they exist

from .base import *

try:
    from .local import *
except ImportError:
    raise Exception('Could not find settings/local.py.'
                    'Please create it and try again')

print SSH_HOST
