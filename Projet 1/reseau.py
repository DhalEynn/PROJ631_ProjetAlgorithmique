# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:12:06 2019

@author: Dahleynn
"""

"""
Split the parameter 'string' by space, N character and + character
"""
def quickSplit(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N' and i != '+'):
            temp.append(i)
    return temp

"""
Regroup all the names "GARE_QUAI_SUD", "GARE_QUAI_EST", "GARE_QUAI_NORD", "GARE_QUAI_OUEST" into the name "QUAI".
"""
def regroupQUAIs (lines):
    errors = ("GARE_QUAI_SUD", "GARE_QUAI_EST", "GARE_QUAI_NORD", "GARE_QUAI_OUEST")
    for line in lines:
        for i in range (len(line)):
            if (line[i] in errors):
                line[i] = "QUAI"
    return lines

"""
Return the difference between t1 and t2 (t2 - t1), or None if the time isn't in the correct format.
"""
def diffTime(t1, t2):
    if (t1 == "-" or t2 == "-"):
        return (None)
    t1 = t1.split(":")
    t2 = t2.split(":")
    if (len(t1)!= 2 or len(t2) != 2):
        return(None)
    diff = int(t2[0]) * 60 + int(t2[1]) - (int(t1[0]) * 60 + int(t1[1]))
    return(diff)

"""
Proceed to the creation of the arcs by spliting a list formed like :
    0 = list of stops, 
    1-k = one stop followed by its schedule in one direction, 
    k-end = the same in the other direction
and returning a list of arcs.
"""
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

"""
Take the processed list from the function arcProcessing and regroup them by the name of the stop in a tuple :
    name of the stop, 
    list of the arcs outputing from this stop in the normal schedule
    list of the arcs outputing from this stop in the holyday schedule
"""
def arcInclusion (processedList, normalArc, holydayArc):
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

"""
Delete the problematical stops coming from 'errors' from the unprocessed list formed like:
    0 - list of stops
    1-end - list with name of the stop on 0 and times on 1+
"""
def errorsClean (unprocessedList, errors):
    # Clean the errors in unprocessedList : stop and its schedule
    temp = []
    for i in range (len(unprocessedList)):
        if (unprocessedList[i][0] in errors and len(unprocessedList[i]) != len(unprocessedList[0])):
            temp.insert(0, i)
    result = unprocessedList
    for i in temp:
        result.pop(i)
    # Clean the errors in unprocessedList : list of stops
    temp = []
    for i in range (len(unprocessedList[0])):
        if (unprocessedList[0][i] in errors):
            temp.insert(0, i)
    for i in temp:
        result[0].pop(i)
    return result



"""
Class Reseau :  the main class of the program
Dependencies :
    - Line
    - Stops
Parameters :
    lines - dictionnary of lines
    stops - dictionnary holding all the stops
    errors - problematical stops
"""
class Reseau:
    def __init__ (self, errors = []):
        self.lines = {}
        self.stops = {}
        self.errors = errors

    def addLine (self, lineNumber, path):
        if (lineNumber in self.lines):
            print("\nThis line already exist")
        else:
            self.lines[lineNumber] = Line(lineNumber, path)
            
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
            normal = lines[:1+numberStop*2]
            holydays = lines[1+numberStop*2:]
    
            # Cleaning the list of stops
    
            normal[0] = quickSplit(normal[0])
            holydays[0] = quickSplit(holydays[0])
    
            # Split the lines of stops
    
            for i in range (1, len(normal)):
                normal[i] = normal[i].split()
            for i in range (1, len(holydays)):
                holydays[i] = holydays[i].split()
            
            if (self.errors != []):
                normal = errorsClean(normal, self.errors)
                holydays = errorsClean(holydays, self.errors)
    
            # Regroup the different QUAI stops
    
            normal = regroupQUAIs(normal) 
            holydays = regroupQUAIs(holydays)
    
            # Arcs creation
    
            normalArcs = arcProcessing(normal, numberStop)
            holydaysArcs = arcProcessing(holydays, numberStop)
    
            # Arc inclusion
    
            inclusion = arcInclusion(normal, normalArcs, holydaysArcs)
            for i in range(0, len(inclusion), 3):
                self.addStop(inclusion[i], inclusion[i+1], inclusion[i+2])
            
            for temp in normal[0]:
                self.lines[lineNumber].stops[temp] = self.stops.get(temp, temp)
                # Adding the stops associated with the line [the (temp, temp) parameter of get is here to add an object Stops, or at least the name if not found]
                    

    def addStop (self, name, arcs = [], holyarcs = []):
        if (name in self.stops):
            self.stops[name].addArc(arcs)
            self.stops[name].addHolyarc(holyarcs)
        else:
            self.stops[name] = Stops(name, arcs, holyarcs)

    # Return a list of the key linked to the lines of Reseau
    def listLines (self):
        temp = []
        for key in self.lines.keys():
            temp.append(key)
        return temp

    # Print the lines with their stops (and their schedule if wanted)
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

    # Print all the stops and their schedule
    def allprintstops (self):
        for key in self.stops.keys():
            print(self.stops[key].name)
            print(self.stops[key].showStop())

    def printStop (self, name):
        self.stops[name].showStop()

    # Return all the lines passing by the stop in parameter
    def usedLine (self, stop):
        result = []
        for key in self.lines.keys():
            if (stop in self.lines[key].stops and not(key in result)):
                    result.append(key)
        return result
                

"""
Class Line :    class which regroup the stops belonging to a line.
                Mainly used for printing
Dependant of :
    - Reseau
Dependencies :
    - Stops
Parameters :
    stops - dictionnary of all the stops of this line
"""
class Line:
    def __init__ (self, number, path):
        self.stops = {}

"""
Class Stops :   class defining the differents stops.
Dependant of :
    - Reseau
    - (Line)
Dependencies :
    - Arcs
Parameters :
    name - name of the stop
    arcs - list of all the arcs outputting from this stop at normal schedule
    holyarcs - list of all the arcs outputting from this stop at holyday schedule
"""
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

    def addArc (self, arclist):
        for arc in arclist:
            self.arcs.append(Arcs(arc))

    def addHolyarc (self, holyarclist):
        for holyarc in holyarclist:
            self.holyarcs.append(Arcs(holyarc))

    # Print the stops
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
                    print(arc.getStart())
                    print(end = '     ')
                else:
                    i += 1
                    print(arc.getStart(), end = ' ')
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
                    print('')
                    print("\n     Direction", temp)
                    print(end = '     ')
                if (i == 4):
                    i = 0
                    print(arc.getStart())
                    print(end = '     ')
                else:
                    i += 1
                    print(arc.getStart(), end = ' ')
            print('')
    
    def printArcs (self):
        for arc in self.arcs:
            arc.printer()
    
    def printHolyarcs (self):
        for arc in self.holyarcs:
            arc.printer()
    
    # Get the weight of the arc going to nextStop which is the closest superior to the time in parameter
    def getMassConditional (self, nextStop, time, holybool):
        if (holybool):
            for arc in self.holyarcs:
                if (diffTime(arc.getStart(), time) != None and diffTime(arc.getStart(), time) >= 0 and arc.getnext() == nextStop):
                   return arc.getMass()
        else:
            for arc in self.arcs:
                if (diffTime(arc.getStart(), time) != None and diffTime(arc.getStart(), time) >= 0 and arc.getnext() == nextStop):
                   return arc.getMass()
        return 999
            

"""
Class Arcs :   class defining the differents edges.
Dependant of :
    - Stops
Parameters :
    comeFrom - starting stop
    goto - going to this stop
    start - starting hour
    end - arrival time
    mass - name of the stop
    EOL - name of the stop
"""
class Arcs:
    def __init__ (self, arc):
        self.comeFrom = arc[0]
        self.goto = arc[1]
        self.start = arc[2]
        self.end = arc[3]
        self.mass = arc[4]
        self.EOL = arc[5]

    def printer (self):
        print(self.comeFrom, self.goto, self.start, self.end, self.mass, self.EOL)
    
    def getAll (self):
        return ((self.comeFrom, self.goto, self.start, self.end, self.mass, self.EOL))
    
    def getnext (self):
        return self.goto
    
    def getMass (self):
        return self.mass
    
    def getStart (self):
        return self.start
    
    def getDest (self):
        return self.EOL
