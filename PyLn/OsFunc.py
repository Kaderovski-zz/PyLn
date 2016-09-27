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

def power_func() :
            
    with open('{0}'.format(Tmp) + 'acpi.txt', 'w') as f:
        oRequest = subprocess.call(['bash', BashFunc + 'acpi.bash'], stdout=f)
   
    with open ('{0}'.format(Tmp) + 'acpi.txt', "r") as retour:
        data=retour.read()
    # Reading from the oSay_func()
    oSay_func_eng('There is ' + data + 'battery left')
    purge('{0}'.format(Tmp), 'acpi.txt') 


# Here is the clear function
def clear_func() :
    tmp = subprocess.call('clear',shell=True)
