# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:45 2019

@author: Dahleynn
"""

import reseau
import algorithms

# Initialisation

errors = ["LYCÉE_DE_POISY"]
Bus = reseau.Reseau(errors)


"""
    Main program ==============================================================
"""

# Open the list of the different lines

mainFile = open("data/_ListLines.txt", "r", encoding="utf-8")
ListLines = mainFile.readlines()
mainFile.close()

# Cleaning ListLines

for i in range (len(ListLines)):
    if (i % 2 == 0):
        ListLines[i] = ListLines[i].split()
        ListLines[i] = ListLines[i][1]
    else:
        ListLines[i] = ListLines[i].rstrip()

# Creating the lines

for i in range (0, len(ListLines), 2):
    Bus.addLine(ListLines[i], ListLines[i + 1])

# Calls

Bus.allprintlines()
toTake = algorithms.princ(Bus, "PISCINE-PATINOIRE", "CAMPUS", "07:45", False)