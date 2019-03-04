# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:12:06 2019

@author: Dahleynn
"""

class Reseau:
    def __init__ (self):
        self.lines = {}
    
    def addLine (self, number, path):
        if (self.lines.get(number)):
            print("This line already exist")
        else:
            self.lines[number] = Line(path)
    
    def listLines (self):
        temp = []
        for key in self.lines.keys():
            temp.append(key)
        return temp
    
    def printlines (self):
        print("Here are the existing lines :")
        for key in self.lines.keys():
            print(key)
        
class Line:
    def __init__ (self, path):
        self.stops = {}
        self.addListStops(path)
        
    def addListStops (path):
        print ("")

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
    
    def showStop (self):
        if (self.arcs != []):
            i = 0
            print ("Normal times :")
            temp = self.arcs[0].getDest()
            print("\nDirection", temp)
            for arc in self.arcs:
                if (temp != arc.getDest()):
                    temp = arc.getDest()
                    print("\nDirection", temp)
                if (i == 4):
                    i = 0
                    print(arc.getTimeStop())
                else:
                    i += 1
                    print(arc.getTimeStop(), end = ' ')
                
            
        
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