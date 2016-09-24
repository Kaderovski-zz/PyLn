#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# List import
# Have to clear it !
import os, sys
import subprocess
import re

# Define the output voice as a function
def oSay_func(arg):
    subprocess.call(['google_speech', '-l', 'en', arg, '-e', 'speed', '1.1'])

# Asking user question :
oQuestion = input("What is your question ? ")


# As we doing a curl from the evi.com/q/ we need to replace spaces with "_"
# print(oQuestion.replace (" ", "_"))
oInput=oQuestion.replace(" ", "_")

# We put the curl's output inside a text.file
with open('tmp/out-file.txt', 'w') as f:
    oRequest = subprocess.call(['curl', '--silent', 'https://www.evi.com/q/' + oInput], stdout=f)

# Convert it in str
oRequests = str(oRequest)

# Here is the regex works bash on the output.txt
# Need to create a Python one to avoir subprocess.call
with open('tmp/retour.txt', 'w') as d:
    oSed = subprocess.call(['bash', 'cut.bash', 'tmp/out-file.txt'], stdout=d)

# In the debug mode, print the output of bash
oContent = subprocess.call(['cat', 'tmp/retour.txt'])

# If there is no answer from the evi.com, the file will be empty
# So we check for the answer 

if os.stat("tmp/retour.txt").st_size == 0:
    #print("This is an empty file")
    oSay_func("Sorry, I do not know the answer.")

else:
    # Preparing to read
    with open ("tmp/retour.txt", "r") as retour:
        data=retour.read()

    # Reding from the oSay_func()
    oSay_func(data)

# After saying, we need to remove the two files : out-file.txt and retour.txt
# We need to segment this function to another file.
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

purge('tmp/', 'txt')

# Todo :
# Preparing the different output format (I saw ther is an h3 html tag that can pass)
