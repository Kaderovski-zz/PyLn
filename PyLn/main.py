#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# List import
# Have to clear it !
import os, sys
import subprocess
import re
from OsFunc import * 
from oSayFunc import *
from oCommonFunc import *
from oPurgeFunc import *

# Define used Path Dir :
BashReg = '../BashReg/'
Tmp = '../tmp/'

while True :

    # Asking user question :
    oQuestion = input("What is your question ? ")

    # I have to create a Function Def for personnal answer
    if oQuestion == "exit" :
        subprocess.call(['google_speech', '-l', 'en', 'It was a pleasure to work with you, see you soon', '-e', 'speed', '1.1'])
        sys.exit()

    # Need to change it to make a Regex Function 
    # That will grep the "battery" word and start it 
    elif oQuestion == "battery" :
        power_func()        

    elif oQuestion == "news" :
        get_the_news_func()

    else :
        # As we doing a curl from the evi.com/q/ we need to replace spaces with "_"
        # print(oQuestion.replace (" ", "_"))
        oInput=oQuestion.replace(" ", "_")

        # We put the curl's output inside a text.file
        with open('{0}'.format(Tmp) + 'out-file.txt', 'w') as f:
            oRequest = subprocess.call(['curl', '--silent', 'https://www.evi.com/q/' + oInput], stdout=f)

        # Convert it in str
        oRequests = str(oRequest)


    
        # We know there is two output : tk_common and tk_text
        # We will make to pattern regex to define the oSayfunc()

        oFind_common = 0
        oFind_text = 0

        with open('{0}'.format(Tmp) + 'out-file.txt') as f:
            for line in f:
                    
                if re.search(r'tk_common', line) is not None:
                    #print("I find tk_common in out-file")
                    oFind_common = 1
                    break

                elif re.search(r'tk_text', line) is not None:
                    #print("I find tk_text in out-file")
                    oFind_text = 1
                    break

                else:
                    pass


        if oFind_common == 1 :
            
            # We start the work    
            # Here is the regex works bash on the output.txt
            # Need to create a Python one to avoir subprocess.call
            
            with open('{0}'.format(Tmp) + 'retour.txt', 'w') as d:
                oSed = subprocess.call(['bash', BashReg + 'cut.bash', Tmp + 'out-file.txt'], stdout=d)

                # In the debug mode, print the output of bash
                oContent = subprocess.call(['cat', '{0}'.format(Tmp) + 'retour.txt'])

                # Preparing to read
                with open ('{0}'.format(Tmp) + 'retour.txt', "r") as retour:
                    data=retour.read()

                    # Reading from the oSay_func()
                    oSay_func(data)


        elif oFind_text == 1 :

            # We start the work    
            # Here is the regex works bash on the output.txt
            # Need to create a Python one to avoir subprocess.call
            
            with open('{0}'.format(Tmp) + 'retour.txt', 'w') as d:
                oSed = subprocess.call(['bash', BashReg + 'cut_h3.bash', Tmp + 'out-file.txt'], stdout=d)

                # In the debug mode, print the output of bash
                oContent = subprocess.call(['cat', '{0}'.format(Tmp) + 'retour.txt'])

                # Preparing to read
                with open ('{0}'.format(Tmp) + "retour.txt", "r") as retour:
                    data=retour.read()

                    # Reading from the oSay_func()
                    oSay_func_eng(data)

        else :
            oSay_func_eng("Sorry, I do not know the answer.")
        
        purge('{0}'.format(Tmp), 'txt')
