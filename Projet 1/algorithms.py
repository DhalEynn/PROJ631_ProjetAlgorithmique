# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:39:15 2019

@author: Dahleynn
"""

# Menu for all the other algorithms of the file

def princ (Bus, Astart, Astop, Hstart, holydayBoolean):
    print("\nYou want to go to", Astop, "from", Astart, "\n")
    #print("1 - Foremost (arrive au plus tôt, peut importe le nombres d'arcs)")
    print("2 - Shortest (le plus court, en nombre d'arcs)")
    #print("3 - Fastest (le plus rapide, mais avec potentiellement plus d'arcs)")
    print("\n")
    test = 0
    """
    while (test < 1 or test > 3):
        test = input("What algorithm do you want to use ?\n")
        try:
            test = int(test)
        except TypeError:
            print("\n   You did not input a number !\n")
            test = 0
    """ # Part used to make the choice between algorithms, temporarily commented
    test = 2 # temporary until the other algorithms are finished
    if (test == 1):
        print("You choose the algorithm foremost")
        return foremost(Bus, Astart, Astop, Hstart, holydayBoolean)
    elif (test == 2):
        print("You choose the algorithm shortest")
        return shortest(Bus, Astart, Astop, holydayBoolean)
    else:
        print("You choose the algorithm fastest")
        return fastest(Bus, Astart, Astop, Hstart)


def foremost (graph, Astart, Astop, Hstart, holydayBoolean):
    print ("foremost")
    print (Astart, Astop, Hstart)


# Use dijsktra algorithm to find the shortest path between initial and end.
# Algorithm base taken from http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/ and adapted to my data structure.

def shortest(graph, initial, end, holydayBoolean):
    # shortest paths is a dictionnary of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
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
            weight = 1 + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    printShortest(graph, path)
    return path


def fastest (Bus, Astart, Astop, Hstart):
    print ("fastest")
    print (Astart, Astop, Hstart)


def printShortest(graph, listShort):
    print("Here is the shortest path to go from", listShort[0], "to", listShort[-1], ", as has been defined by \"the shortest path in the number of edges\"\n")
    for stop in listShort:
        listLines = graph.usedLine(stop)
        if (len(listLines) > 1):
            print("Lines", listLines[0], end = '')
            for line in range(1, len(listLines)):
                print(",", listLines[line], end='')
            print(" -", stop)
        else:
            print ("Line", listLines[0], "-", stop)
    print("Number of stops :", len(listShort))