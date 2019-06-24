import time

emptyMarker = " "
filledMarker = "*"
escapeMarker = "E"


#Funktion: Öffnen einer datei und umwandlung in field
def fileToField(filename):
    ftf = []
    f = open(filename, "r")
    line = f.readline()
    while line:
        ftf.append(list(line[:-1]))
        line = f.readline()
    f.close()
    return ftf

field = fileToField("field2.txt")

#Funktion: Ausgabe des Feldes
def printField(field):
    print()
    for i in range(len(field)):
        for j in range(len(field[0])):
            print(field[i][j], end = "")
        print()

#Prüfe ob die Stelle im Feld keine Wand ist
def isFree(row, col):
    if field[row][col] is emptyMarker or field[row][col] is escapeMarker:
        return True
    else:
        return False

#Prüfe ob die Stelle im Feld das Ziel ist
def isEscape(row, col):
    if field[row][col] is escapeMarker:
        return True
    else:
        return False

#Prüfe ob die Stelle innerhalb des Feldes ist
def isWithin(row, col):
    if row >= 0 and row < len(field) and col >= 0 and col < len(field):
        return True
    else:
        return False

#Funktion: Kürzesten Weg aus Routen finden
def shortestRoute(route):
    minR = len(route[0])
    shortest = route[0]
    for i in range(0, len(route)):
        if len(route[i]) < minR:
            minR = len(route[i])
            shortest = route[i]
    return shortest

#Funktion: Startet Suche nach dem Ausgang/Ziel
def findEscape(rowNum, colNum, route=()):
    route += ((rowNum, colNum),)
    if isEscape(rowNum, colNum) is True:
        return route

    routeEscape = []
    adjacent = ((0, 1), (0, -1), (1, 0), (-1, 0))

    for i in adjacent:
        adjRow = rowNum + i[0]
        adjCol = colNum + i[1]
        tempR = []
        if isWithin(adjRow, adjCol) is True and isFree(adjRow, adjCol) is True:
            if (adjRow, adjCol) not in route:
                tempR = findEscape(adjRow, adjCol, route)
                if len(tempR) > 0:
                    routeEscape.append(tempR)

    if len(routeEscape) == 0:
        return ();

    pathSol = shortestRoute(routeEscape)
    return pathSol

#Zeitmessung für Aufgabe 11
time1 = time.perf_counter()
path = findEscape(1, 1)
time2 = time.perf_counter()
timeFinal = time2 - time1

#Zeichensetzung für den Weg
for p in path:
    field[p[0]][p[1]] = filledMarker

#Ausgabe von Feld, Weg und Zeit
printField(field)
print("----------")
print("Feld Koordinaten des Weges:", path)
print("Gemessene Zeit der Funktion:", timeFinal, "s")
print("----------")