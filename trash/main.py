# -*- coding: utf-8 -*-
def quickSplitN(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N'):
            temp.append(i)
    return temp

def printer(lines, number):
    for i in range(number):
        print(lines[i])

def divineCreation (path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    temp = []
    for i in range (len(lines)):
        if (lines[i] == '\n'):
            temp.insert(0, i)
    for i in temp:
        lines.pop(i)
    lines[0] = quickSplitN(lines[0])
    numberStop = len(lines[0])
    for i in range (1, 1 + numberStop * 2):
        lines[i] = lines[i].split()
    printer(lines, numberStop + 1)  #===== Ajout arcs ici

divineCreation("data/2_Piscine-Patinoire_Campus.txt")