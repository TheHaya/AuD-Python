import time

emptyMarker = " "
filledMarker = "x"
escapeMarker = "E"


#Funktion: Öffnen einer datei und umwandlung in field
def fileToField(filename):
    ftf = []
    f = open("fileName", "r")
    line = f.readline()
    while line:
        ftf.append()
        line = f.readline()
    f.close()
    return ftf

field = fileToField("field3.txt")

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
def tileEscape(row, col):
    if field[row][col] is escapeMarker:
        return True
    else:
        return False

#Prüfe ob die Stelle innerhalb des Feldes ist
def tileWithin(row, col):
    if row >= 0 and row < len(field) and col >= 0 and col < len(field):
        return True
    else:
        return False

#fdf
