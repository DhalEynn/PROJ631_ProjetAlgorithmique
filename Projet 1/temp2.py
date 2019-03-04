# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:45 2019

@author: Dahleynn
"""

def quickSplit(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N' and i != '+'):
            temp.append(i)
    return temp

def regroupQUAIs (lines):
    errors = ("GARE_QUAI_SUD", "GARE_QUAI_EST", "GARE_QUAI_NORD", "GARE_QUAI_OUEST")
    for line in lines:
        for i in range (len(line)):
            if (line[i] in errors):
                line[i] = "QUAI"
    return lines

"""
def numberedPrinter (lines, number):
    for i in range(number):
        print(lines[i])
"""     
def printer (lines):
    for i in lines:
        print(i)

def diffTime(t1, t2):
    if (t1 == "-" or t2 == "-"):
        return (None)
    t1 = t1.split(":")
    t2 = t2.split(":")
    if (len(t1)!= 2 or len(t2) != 2):
        return(None)
    diff = int(t2[0]) * 60 + int(t2[1]) - (int(t1[0]) * 60 + int(t1[1]))
    return(diff)




path = "data/2_Piscine-Patinoire_Campus.txt" 
#2_Piscine-Patinoire_Campus | 1_Poisy-ParcDesGlaisins
file = open(path, "r", encoding="utf-8")
lines = file.readlines()
file.close()

# Clear the \n of the file

temp = []
for i in range (len(lines)):
    if (lines[i] == '\n'):
        temp.insert(0, i)
for i in temp:
    lines.pop(i)

# Split the file in normal and holyday times

numberStop = len(quickSplit(lines[0]))
normal = lines[:1+numberStop*2]
#holydays = lines[1+numberStop*2:]

# Cleaning the list of stops

normal[0] = quickSplit(normal[0])
#holydays[0] = quickSplit(holydays[0])

# Split the lines of stops

for i in range (1, len(normal)):
    normal[i] = normal[i].split()
"""for i in range (len(holydays)):
    holydays[i] = holydays[i].split()"""

# Regroup the different QUAI stops

normal = regroupQUAIs(normal)

# Split the ways of the line (A to B, B to A)

goto = normal[1:numberStop+1]
gofrom = normal[numberStop+1:]

# Arc creation

arc = []
for line in range (len(goto) - 1):
    actual = goto[line]
    anextL = goto[line + 1]
    for idTime in range (1, len(actual)):
        differ = diffTime(actual[idTime], anextL[idTime])
        if (differ != None):
            arc.append((actual[0], anextL[0], actual[idTime], anextL[idTime], differ, normal[0][-1]))
for line in range (len(gofrom) - 1):
    actual = gofrom[line]
    anextL = gofrom[line + 1]
    for idTime in range (1, len(actual)):
        differ = diffTime(actual[idTime], anextL[idTime])
        if (differ != None):
            arc.append((actual[0], anextL[0], actual[idTime], anextL[idTime], differ, normal[0][0]))

