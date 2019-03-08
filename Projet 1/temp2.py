# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:18:45 2019

@author: Dahleynn
"""

import reseau

errors = ["LYCÉE_DE_POISY"]
Bus = reseau.Reseau(errors)

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


def addingTime (time, weight):
    time = time.split(":")
    if (len(time)!= 2):
        return(None)
    try:
        minutes = int(time[0]) * 60 + int(time[1]) + int(weight)
    except TypeError:
        return time
    return (str(int(minutes / 60)) + ":" + str(int(minutes % 60)))

def printForemost (couple):
    if (len(couple[0]) == len(couple[1])):
        print("Here are your stops :")
        for key in range (len(couple[0])):
            print(couple[0][key], "-", couple[1][key])
    

def foremost(graph, initial, end, time, holydayBoolean):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0, time)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        
        temp = []
        if (holydayBoolean):
            for arc in graph.stops[current_node].holyarcs:
                if (not(arc.getnext() in temp)):
                    temp.append(arc.getnext())
        else:
            for arc in graph.stops[current_node].arcs:
                if (not(arc.getnext() in temp)):
                    temp.append(arc.getnext())
                    
        destinations = temp
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            value = graph.stops[current_node].getMassConditional(next_node, time, holydayBoolean)
            weight = value + weight_to_current_node
            print(time, value)
            if (value != 999): # Semantically wrong value
                time = addingTime(time, value)
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight, time)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight, time)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    schedule = []
    current_time = time
    while current_node is not None:
        path.append(current_node)
        schedule.append(current_time)
        next_node = shortest_paths[current_node][0]
        next_time = shortest_paths[current_node][2]
        current_node = next_node
        current_time = next_time
    # Reverse path
    path = path[::-1]
    schedule = schedule[::-1]
    return ((path, schedule))

#Bus.allprintlines()
    
toTake = foremost(Bus, "PISCINE-PATINOIRE", "CAMPUS", "07:45", False)
printForemost(toTake)
print(toTake)