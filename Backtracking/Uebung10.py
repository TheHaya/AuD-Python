import copy
import os
import time

emptyMarker = " "
escapeMarker = "E"
fillMarker = "."


def convertFileToField(filename):
    f = open(filename, "r")
    line = f.readline()
    fld = []
    while line:
        fld.append(list(line[:-1]))
        line = f.readline()
    f.close
    return fld


def printField(f):
    print()
    for i in range(0, len(f)):
        for n in range(0, len(f[0])):
            print(f[i][n], end='')
        print()


def isFree(r, c):
    if field[r][c] == emptyMarker or field[r][c] == escapeMarker:
        return True
    else:
        return False


def isEscape(r, c):
    if field[r][c] == escapeMarker:
        return True
    else:
        return False


def isInField(r, c):
    if r >= 0 and r < len(field) and c >= 0 and c < len(field):
        return True
    else:
        return False


def minWeg(route):
    minimum = len(route[0])
    short = route[0]
    for i in range(1, len(route)):
        if (len(route[i]) < minimum):
            minimum = len(route[i])
            short = route[i]
    return short


def findEscape(r, c, route=()):
    route += ((r, c),)

    if isEscape(r, c):
        return route

    relativeN = ((0, 1), (0, -1), (1, 0), (-1, 0))
    escapeRoutes = []
    for rN in relativeN:
        nr = r + rN[0]
        nc = c + rN[1]
        if isInField(nr, nc) and isFree(nr, nc) and not (nr, nc) in route:
            tmp = findEscape(nr, nc, route)
            if len(tmp) > 0:
                escapeRoutes += [tmp]

    if len(escapeRoutes) == 0:
        return ();
    kuerzesteWeg = minWeg(escapeRoutes)
    return kuerzesteWeg


field = convertFileToField("field3.txt")
zeit1 = time.clock()
route = findEscape(1, 1)
zeit2 = time.clock()
for p in route[:-1]:
    field[p[0]][p[1]] = fillMarker
printField(field)
print("\nKoordinaten der kuerzesten Weg: ", route)
print("\nZeit: ", zeit2 - zeit1)
