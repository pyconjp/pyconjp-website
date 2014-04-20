#:coding=utf-8:

# This just exists to have something to use as a default settings
# that will try to use local.py and give a useful error
# message if not found.

import sys

try:
    from .local import *  # NOQA
except ImportError:
    print("ERROR: A pycon/settings/local.py file is required but was "
          "not found.")
    print("You can copy local.py-example to local.py "
          "and edit it according to the comments.")
    sys.exit(1)
