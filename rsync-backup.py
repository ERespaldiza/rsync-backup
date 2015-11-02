#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
rsync-backup.py
Incremental Backups with rsync
usage: python rsync-backup.py SRC DEST [--prefix] [OPTIONS]
"""

import os
import sys
import datetime
import six

__author__ = "Eugenio Respaldiza <eugenio.respaldiza@gmx.com>"
__maintainer__ = "Eugenio Respaldiza"
__copyright__ = "Copyright (C) 2015"
__license__ = "GPL"
__status__ = "Production"  # Prototype, Development
__version__ = "1.0.0"
__date__ = ""

SOURCE = sys.argv[1] if sys.argv[1][-1:] == '/' else sys.argv[1] + '/'
TARGET = sys.argv[2] if sys.argv[2][-1:] == '/' else sys.argv[2] + '/'
NOW = datetime.datetime.now().strftime("%y%m%d_%H%M")
PREFIX = '__bak_'
# Allow override PREFIX with --prefix option
for arg in sys.argv[3:]:
    items = arg.split('=')
    if items[0] == '--prefix':
        PREFIX = items[1]
        sys.argv.remove(arg)

EXCLUDE_PATTERN = PREFIX + '*'
BACKUP_DIR = TARGET + PREFIX + NOW + '/'
# Prevent paths with spaces adding double quotes
RSYNC_COMMAND = \
    " ".join(("rsync", "\"" + SOURCE + "\"", "\"" + TARGET + "\""))
# Default backup options.
BACKUP_OPTIONS = {'--archive': '', '--backup': '', '--backup-dir': BACKUP_DIR,
                  '--delete': '', '--hard-links': '',
                  '--exclude': EXCLUDE_PATTERN, '--checksum': ''}

# Bypass more rsync options from command line and allow override --backup-dir
# and --exclude.
for arg in sys.argv[3:]:
    items = arg.split('=')
    if len(items) == 1:
        BACKUP_OPTIONS[items[0]] = ''
    else:
        BACKUP_OPTIONS[items[0]] = items[1]

# Generate rsync command
# Note six.iteritems() for python 2.7 and 3 compatibility
for k, v in six.iteritems(BACKUP_OPTIONS):
    RSYNC_COMMAND += ' ' + k
    if v != '':
        RSYNC_COMMAND += '=' + v

# Create directories
if '--dry-run' not in BACKUP_OPTIONS:
    if not os.path.exists(TARGET):
        os.makedirs(TARGET)

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

code = os.system(RSYNC_COMMAND)
sys.exit(code)
