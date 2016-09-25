#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# List import
# Have to clear it !
import os, sys
import subprocess
import re

# Define All Func needed
#
# Define the output voice as a function
def oSay_func(arg):
    subprocess.call(['google_speech', '-l', 'en', arg, '-e', 'speed', '1.1'])
    return

# Define delete function
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

while True :

    # Asking user question :
    oQuestion = input("What is your question ? ")

    # I have to create a Function Def for personnal answer
    if oQuestion == "exit" :
        subprocess.call(['google_speech', '-l', 'en', 'It was a pleasur to work with you, see you soon', '-e', 'speed', '1.1'])
        sys.exit()

    else :
        # As we doing a curl from the evi.com/q/ we need to replace spaces with "_"
        # print(oQuestion.replace (" ", "_"))
        oInput=oQuestion.replace(" ", "_")

        # We put the curl's output inside a text.file
        with open('../tmp/out-file.txt', 'w') as f:
            oRequest = subprocess.call(['curl', '--silent', 'https://www.evi.com/q/' + oInput], stdout=f)

        # Convert it in str
        oRequests = str(oRequest)


    
        # We know there is two output : tk_common and tk_text
        # We will make to pattern regex to define the oSayfunc()

        oFind_common = 0
        oFind_text = 0

        with open("../tmp/out-file.txt") as f:
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
            
            with open('../tmp/retour.txt', 'w') as d:
                oSed = subprocess.call(['bash', '../BashReg/cut.bash', '../tmp/out-file.txt'], stdout=d)

                # In the debug mode, print the output of bash
                oContent = subprocess.call(['cat', '../tmp/retour.txt'])

                # Preparing to read
                with open ("../tmp/retour.txt", "r") as retour:
                    data=retour.read()

                    # Reading from the oSay_func()
                    oSay_func(data)


        elif oFind_text == 1 :

            # We start the work    
            # Here is the regex works bash on the output.txt
            # Need to create a Python one to avoir subprocess.call
            
            with open('../tmp/retour.txt', 'w') as d:
                oSed = subprocess.call(['bash', '../BashReg/cut_h3.bash', '../tmp/out-file.txt'], stdout=d)

                # In the debug mode, print the output of bash
                oContent = subprocess.call(['cat', '../tmp/retour.txt'])

                # Preparing to read
                with open ("../tmp/retour.txt", "r") as retour:
                    data=retour.read()

                    # Reading from the oSay_func()
                    oSay_func(data)

        else :
            oSay_func("Sorry, I do not know the answer.")


        purge('../tmp/', 'txt')
