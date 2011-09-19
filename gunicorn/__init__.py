# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license. 
# See the NOTICE for more information.

version_info = (0, 13, 3)
__version__ = ".".join(map(str, version_info))
SERVER_SOFTWARE = "gunicorn/%s" % __version__
