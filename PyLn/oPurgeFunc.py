#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

import os, sys
import re

# Define delete function
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))


