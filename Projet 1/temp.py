def quickSplitN(string):
    string = string.split()
    temp = []
    for i in string:
        if (i != 'N'):
            temp.append(i)
    return temp

path = "data/2_Piscine-Patinoire_Campus.txt"
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
numberStops = len(lines[0])
for i in range (1, 1 + numberStops * 2):
    lines[i] = lines[i].split()
holyday = 2 + numberStops * 2
print(lines[1][1])
temp = lines[1][1].split(":")
temp = int(temp[0]) * 60 + int(temp[1])
print(temp)