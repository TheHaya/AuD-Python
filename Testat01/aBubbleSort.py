import time

def bubbleSort(L):

    tStart = time.clock()

    swapped = True

    while swapped == True:
        swapped = False
        for i in range(0, len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True

    tEnd = time.clock()
    tSum = tEnd - tStart

    return tSum
