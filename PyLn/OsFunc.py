#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# List import
# Have to clear it !
import os, sys
import subprocess
import re

# Define used Path Dir :
BashFunc = '../BashFunc/'
Tmp = '../tmp/'

def power_func() :
    power = subprocess.call(['bash', BashFunc + 'acpi.bash'])
    return

