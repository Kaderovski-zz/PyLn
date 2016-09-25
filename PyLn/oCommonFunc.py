#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# List import
# Have to clear it !
import os, sys
import subprocess
import re
from oSayFunc import *
from oPurgeFunc import *


# Define used Path Dir :
BashFunc = '../BashFunc/'
Tmp = '../tmp/'


# Here is a function to get the News from 
# French newspaper LeMonde.fr

def get_the_news_func() :
            
    with open('{0}'.format(Tmp) + 'news.txt', 'w') as f:
        oRequest = subprocess.call(['bash', BashFunc + 'news.bash'], stdout=f)
   
    with open ('{0}'.format(Tmp) + 'news.txt', "r") as retour:
        data=retour.read()
    # Reading from the oSay_func()
    oSay_func_fr('Actualités.' + data)
    purge('{0}'.format(Tmp), 'news.txt') 

