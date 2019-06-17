import random

def testListsGenerator(maxLength):

    List = []
    maxNumbers = 4

    for i in range(0, maxLength):
        testlist = []
        for j in range(0, maxNumbers):
            testlist.append(random.randint(0, 99))
        List.append(testlist)
        testlist.copy()

    return List


