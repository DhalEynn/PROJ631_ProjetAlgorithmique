# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:12:06 2019

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

def arcProcessing (unprocessedList, numberStop):
# Split the ways of the line (A to B, B to A)
    goto = unprocessedList[1:numberStop+1]
    gofrom = unprocessedList[numberStop+1:]
# Arc creation
    arc = []
    for line in range (len(goto) - 1):
        actual = goto[line]
        anextL = goto[line + 1]
        for idTime in range (1, len(actual)):
            differ = diffTime(actual[idTime], anextL[idTime])
            if (differ != None):
                arc.append((actual[0], anextL[0], actual[idTime], anextL[idTime], differ, unprocessedList[0][-1]))
    for line in range (len(gofrom) - 1):
        actual = gofrom[line]
        anextL = gofrom[line + 1]
        for idTime in range (1, len(actual)):
            differ = diffTime(actual[idTime], anextL[idTime])
            if (differ != None):
                arc.append((actual[0], anextL[0], actual[idTime], anextL[idTime], differ, unprocessedList[0][0]))
# End
    return arc

def arcInclusion (processedList, normalArc, holydayArc): # processedList, arcList
    result = []
    for stop in processedList[0]:
        tempArc = []
        tempHoly = []
        for arc in normalArc:
            if (arc[0] == stop):
                tempArc.append(arc)
        for arc in holydayArc:
            if (arc[0] == stop):
                tempHoly.append(arc)
        result.extend((stop, tempArc, tempHoly))
    return result






class Reseau:
    def __init__ (self):
        self.lines = {}
    
    def addLine (self, number, path):
        if (number in self.lines):
            print("\nThis line already exist")
        else:
            self.lines[number] = Line(number, path) 
    
    def listLines (self):
        temp = []
        for key in self.lines.keys():
            temp.append(key)
        return temp
    
    def allprintlines (self):
        temp = input("Do you want the schedule of the stops ? (y or n)\n")
        for key in self.lines.keys():
            print("\nLine", key, "\n")
            for keystop in self.lines[key].stops.keys():
                if (temp == "y"):
                    print("\n-", self.lines[key].stops[keystop].name, ":")
                    self.lines[key].stops[keystop].showStop()
                else:
                    print("-", self.lines[key].stops[keystop].name)
        
class Line:
    def __init__ (self, number, path):
        self.stops = {}
        self.addListStops(number, path)
        
    def addListStops (self, lineNumber, path):
        path = "data/" + path + ".txt"
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
        Anormal = lines[:1+numberStop*2]
        holydays = lines[1+numberStop*2:]
        
        # Cleaning the list of stops
        
        Anormal[0] = quickSplit(Anormal[0])
        holydays[0] = quickSplit(holydays[0])
        
        # Split the lines of stops
        
        for i in range (1, len(Anormal)):
            Anormal[i] = Anormal[i].split()
        for i in range (1, len(holydays)):
            holydays[i] = holydays[i].split()
            
        # Regroup the different QUAI stops
            
        Anormal = regroupQUAIs(Anormal)
        holydays = regroupQUAIs(holydays)
        
        # Arcs creation
        
        AnormalArcs = arcProcessing(Anormal, numberStop)
        holydaysArcs = arcProcessing(holydays, numberStop)
        
        # Arc inclusion
        
        inclusion = arcInclusion(Anormal, AnormalArcs, holydaysArcs)
        for i in range(0, len(inclusion), 3):
            self.addStop(inclusion[i], inclusion[i+1], inclusion[i+2])
    
    def addStop (self, name, arcs = [], holyarcs = []):
        if (name in self.stops):
            self.stops[name].addArc(arcs)
            self.stops[name].addHolyarc(holyarcs)
        else:
            self.stops[name] = Stops(name, arcs, holyarcs)

class Stops:
    def __init__ (self, name, arcs = [], holyarcs = []):
        self.name = name
        # Arcs at normal time
        if (arcs == []):
            self.arcs = arcs
        else:
            temp = []
            for arc in arcs:
                temp.append(Arcs(arc))
            self.arcs = temp
        # Arcs for holydays
        if (holyarcs == []):
            self.holyarcs = holyarcs
        else:
            temp = []
            for arc in holyarcs:
                temp.append(Arcs(arc))
            self.holyarcs = temp
        
    def addArc (self, arc):
        self.arcs.append(Arcs(arc))
        
    def addHolyarc (self, holyarc):
        self.holyarcs.append(Arcs(holyarc))
    
    def showStop (self):
        if (self.arcs != []):
            i = 0
            print ("\n   Normal schedule :")
            temp = self.arcs[0].getDest()
            print("\n     Direction", temp)
            print(end = '     ')
            for arc in self.arcs:
                if (temp != arc.getDest()):
                    i = 0
                    temp = arc.getDest()
                    print('')
                    print("\n     Direction", temp)
                    print(end = '     ')
                if (i == 4):
                    i = 0
                    print(arc.getTimeStop())
                    print(end = '     ')
                else:
                    i += 1
                    print(arc.getTimeStop(), end = ' ')
            print('')
        if (self.holyarcs != []):
            i = 0
            print ("\n   Holyday schedule :")
            temp = self.holyarcs[0].getDest()
            print("\n     Direction", temp)
            print(end = '     ')
            for arc in self.holyarcs:
                if (temp != arc.getDest()):
                    i = 0
                    temp = arc.getDest()
                    print("\n     Direction", temp)
                    print(end = '     ')
                if (i == 4):
                    i = 0
                    print(arc.getTimeStop())
                    print(end = '     ')
                else:
                    i += 1
                    print(arc.getTimeStop(), end = ' ')
            print('')
                
            
        
class Arcs:
    def __init__ (self, arc):
        self.comeFrom = arc[0]
        self.goto = arc[1]
        self.start = arc[2]
        self.end = arc[3]
        self.mass = arc[4]
        self.EOL = arc[5] #End of line
    
    def printer (self):
        print(self.comeFrom, self.goto, self.start, self.end, self.mass, self.EOL)
    
    def getTimeStop (self):
        return self.start
    
    def getDest (self):
        return self.EOL