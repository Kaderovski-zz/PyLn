#!/usr/bin/python
# Dev par Cdiez50

# -*- coding: utf-8 -*-

# Liste des Import à prévoir pour le bon fonctionnement applicatif
import os, sys
import subprocess
import re

# Définition de la function de lecture
def oSay_func(arg):
    subprocess.call(['google_speech', '-l', 'en', arg, '-e', 'speed', '1.1'])

# On attend l'entrée utilisateur
oQuestion = input("What is your question ? ")


# On remplace avec underscore
#print(oQuestion.replace (" ", "_"))
oInput=oQuestion.replace(" ", "_")

# On indique le retour du curl en text "out-file.txt"
with open('out-file.txt', 'w') as f:
    oRequest = subprocess.call(['curl', '--silent', 'https://www.evi.com/q/' + oInput], stdout=f)

# On converti en str
oRequests = str(oRequest)

# On va lire le retour.txt en faisant le travail de sortie du cut.bash
with open('retour.txt', 'w') as d:
    oSed = subprocess.call(['bash', 'cut.bash', 'out-file.txt'], stdout=d)

# Pour afficher la réponse également
oContent = subprocess.call(['cat', 'retour.txt'])

# Préparation du fichier retour à lire
with open ("retour.txt", "r") as retour:
    data=retour.read()

# Lecture
oSay_func(data)


# il faut préparer l'éventualité de la réponse non trouvée
# tk_not_answered
