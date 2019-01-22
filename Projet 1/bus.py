def quickSplitN(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N'):
            temp.append(i)
    return temp

def divineCreation (path):
    """
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    print(lines[0], lines[1], lines[2])
    temp = []
    for i in range (len(lines)):
        if (lines[i] == '\n'):
            temp.append(i)
    for i in temp:
        lines.pop(i)
    print(lines[0], lines[1], lines[2])
    """
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
    nombreArrets = len(lines[0])
    for i in range (1, 1 + nombreArrets * 2):
        lines[i] = lines[i].split()
    print(lines[0], lines[1:13])  #===== Ajout arcs ici

divineCreation("data/2_Piscine-Patinoire_Campus.txt")