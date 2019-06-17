import time

def selectionSort(L):

    tStart = time.clock()

    temp = 0
    for i in range(len(L)):
        minIndex = i
        for e in range(i, len(L)):
            if L[minIndex] > L[e]:
                minIndex = e

        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp

    tEnd = time.clock()
    tSum = tEnd - tStart

    return tSum


