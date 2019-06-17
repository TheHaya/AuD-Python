import matplotlib.pyplot
import aBubbleSort
import aInsertionSort
import aSelectionSort
import bTestListsGenerator

maxNumbers = 100

def plot():
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)


    bubbleList = [bTestListsGenerator.testListsGenerator(i) for i in range(0, maxNumbers)]

    insertionList = [bTestListsGenerator.testListsGenerator(i) for i in range(0, maxNumbers)]

    selectionList = [bTestListsGenerator.testListsGenerator(i) for i in range(0, maxNumbers)]


    ax.plot([i for i in range(0, maxNumbers)], [aBubbleSort.bubbleSort(j) for j in bubbleList], '.', color='r')
    ax.plot([i for i in range(0, maxNumbers)], [aInsertionSort.insertionSort(j) for j in insertionList], '.', color='g')
    ax.plot([i for i in range(0, maxNumbers)], [aSelectionSort.selectionSort(j) for j in selectionList], '.', color='b')

    ax.legend(['Bubble Sort', 'Insertion Sort', 'Selection Sort'])
    ax.set_ylabel('Zeit in s')
    ax.set_xlabel('Anzahl Elemente')

    matplotlib.pyplot.show()

def main():
    plot()

main()