# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:45 2019

@author: Dahleynn
"""

import reseau
Bus = reseau.Reseau()

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

for i in range (0, len(ListLines), 2):
    Bus.addLine(ListLines[i], ListLines[i + 1])

#Bus.allprintlines()
#Bus.stops["QUAI"].printArcs()
#Bus.allprintstops()
Bus.printStop("QUAI")