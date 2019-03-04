from bus import busStop, link

def quickSplitN(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N'):
            temp.append(i)
    return temp

def printer(lines, number, initial = 0):
    for i in range(initial, number):
        print(lines[i])
    
def timeStrToInt(time):
    return (int(time[0]) * 60 + int(time[1]))
    
def arcLister(lines, number, startNumber = 0):
    number += startNumber
    temp = []
    for i in range(startNumber, number):
        if (lines[i][0] != lines[i + 1][0]):
            value = lines[i]
            value2 = lines[i + 1]
            for ptr in range(1, len(value)):
                if (value[ptr] != '-' and value2[ptr] != '-'):
                    calc1 = timeStrToInt(value[ptr].split(":"))
                    calc2 = timeStrToInt(value2[ptr].split(":"))
                    temp.append((value[0], value2[0], value[ptr], value2[ptr], calc2 - calc1))
            temp.append("sep")
    return temp

def listSplitter (value, separateur):
    temp = []
    temp2 = []
    for val in value:
        if(val != separateur):
            temp2.append(val)
        else:
            temp.append(temp2)
            temp2 = []
    return temp

def arcBuild (lines, numberStop, freeday):
    listArcs = arcLister(lines, numberStop * 2)
    #printer(listArcs, len(listArcs))
    listArcs = listSplitter(listArcs, "sep")
    listBusStop = []
    for target in listArcs:
        temp = []
        for arc in target:
            temp.append(link(arc, freeday))
        listBusStop.append(busStop())
        

path = "data/2_Piscine-Patinoire_Campus.txt"
file = open(path, "r")
lines = file.readlines()
file.close()
temp = []
# List all the index where there is only a end of line character.
for i in range (len(lines)):
    if (lines[i] == '\n'):
        temp.insert(0, i)
# Pop listed index
for i in temp:
    lines.pop(i)
# Split the list of names of the stops
lines[0] = quickSplitN(lines[0])
numberStop = len(lines[0])
for i in range (1, 1 + numberStop * 2):
    lines[i] = lines[i].split()
printer(lines, numberStop + 1)
#===== Ajout Arcs
    # Building arcs : (nameFrom, nameTo, timeFrom, timeTo, weight)

#===== Fin Ajout Arcs







"""holyday = 1 + numberStop * 2 #use holyday + numberStop * 2 for freeday listArcs
print(lines[1][1])
temp = lines[1][1].split(":")
temp = int(temp[0]) * 60 + int(temp[1])
print(temp)"""