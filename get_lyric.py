#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sys[argv] 1 = artist, 2 = title, 3 = album
# wrapper for deadbeef infobar plugin
# need glyrc

from sys import argv
import os
import subprocess
import urllib.parse

PATH = '$HOME/.cache/deadbeef/lyrics'
artist = urllib.parse.unquote(argv[1].replace('_', ' '))
title = urllib.parse.unquote(argv[2].replace('_', ' '))
FILEPATH = os.path.join(PATH, artist + '-' + title)
if os.path.exists(FILEPATH):
    with open(FILEPATH, 'r') as outfile:
        print(outfile.read())
else:
    process = subprocess.Popen(['glyrc', 'lyrics', '-v0', '-w',
                                'stdout', '-a', artist, '-t', title])
    retcode = process.wait()
