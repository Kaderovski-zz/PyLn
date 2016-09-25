#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

import subprocess

def oSay_func_eng(arg):
    subprocess.call(['google_speech', '-l', 'en', arg, '-e', 'speed', '1.1'])
    return

def oSay_func_fr(arg):
    subprocess.call(['google_speech', '-l', 'fr', arg, '-e', 'speed', '1.2'])
    return

