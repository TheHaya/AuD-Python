import time

def insertionSort(L):

    tStart = time.clock()

    sortL = []
    for e in L:
        inserted = False
        for listEle in range(len(sortL)):
            if sortL[listEle] > e:
                sortL.insert(listEle, e)
                inserted = True
                break
        if inserted == False:
            sortL.append(e)

    tEnd = time.clock()
    tSum = tEnd - tStart

    return tSum
