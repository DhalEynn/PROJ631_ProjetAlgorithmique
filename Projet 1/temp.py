# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:45 2019

@author: Dahleynn
"""

import reseau
#import algorithms

errors = ["LYCÉE_DE_POISY"]
Bus = reseau.Reseau(errors)

def shortest (Bus, startingStop, endingStop, startingTime):
    return mainShortest(Bus, [], startingStop, endingStop, startingTime, 0)

def mainShortest (Bus, listStops, actualStop, desiredStop, actualTime, nbArcs):
    if (actualStop == desiredStop):
        nbArcs = nbArcs + 1
        listStops.append(actualStop)
        return (listStops, nbArcs)
    if (not(actualStop in listStops)):
        nbArcs = nbArcs + 1
        listStops.append(actualStop)
        usedStop = []
        listArcs = []
        for arc in Bus.stops["actualStop"].arcs:
            temp = arc.getAll()
            if (actualTime < temp[2] and not(temp[1] in usedStop)): 
                # starting time of the arc & goto stop (next stop)
                usedStop.append(temp[1])
                listArcs.append(temp)
        for arc in listArcs:
            mainShortest
        





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
#Bus.printStop("QUAI")