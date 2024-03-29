import itertools
import numpy as np

"""

This file is to store the functions relating to latin_squares containing
tests to check if a square is latin, if a row is latin, and to generate
latin squares.

To generate latin squares, use the function: generateArrayOfLatinSquares(sizeOfSquare)
Replacing the parameter with the integer amount of the desired size of latin square
you want to generate.

e.g. 
    arrayOfLatinSquaresSizeThree = generateArrayOfLatinSquares(3)

"""


def isValidRow(square):
    for row in square:
        if not isValid(row):
            return False
    return True


def isValidColumn(square):
    for col in zip(*square):
        if not isValid(col):
            return False
    return True


def isValid(array):
    for i in range(len(array)):
        if (array[i] > len(array)) or (array[i] < 0):
            return False
    return len(array) == len(set(array))


def isValidLatinSquare(square):
    return isValidRow(square) and isValidColumn(square)


def isValidReducedLatinSquare(square):
    rotated = np.array(square)
    validRow = [i for i in range(1, len(square) + 1)]

    return (validRow == square[0]) and (square[0] == rotated[:, 0]).any() and isValidLatinSquare(square)


def generateValidRows(row):
    return list(itertools.permutations(row))


def generateArrayOfLatinSquares(sizeOfSquare):
    if sizeOfSquare == 0:
        return []
    elif sizeOfSquare == 1:
        return [0]

    row = [i for i in range(1, sizeOfSquare+1)]
    totalSum = sum(row)
    validRows = generateValidRows(row)
    generatedLatinSquares = []
    defaultArray = [[0 for i in range(sizeOfSquare)]
                    for i in range(sizeOfSquare)]
    currentLatinSquare = defaultArray

    n = sizeOfSquare - 1

    dynamicArray = [0 for i in range(n+1)]

    MAX = len(validRows)
    p = 0

    while dynamicArray[n] == 0:

        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):
            for i in range(sizeOfSquare):
                currentLatinSquare[i] = validRows[dynamicArray[i]]

            newRow = []
            sumOfCurrentColumns = 0
            for column in range(sizeOfSquare):
                for row in range(sizeOfSquare-1):
                    sumOfCurrentColumns += currentLatinSquare[row][column]
                newRow.append(totalSum - sumOfCurrentColumns)
                sumOfCurrentColumns = 0
            currentLatinSquare[sizeOfSquare - 1] = tuple(newRow)

            copyOfCurrentLatinSquare = currentLatinSquare[:]
            if(isValidLatinSquare(currentLatinSquare)):
                generatedLatinSquares.append(copyOfCurrentLatinSquare)
            currentLatinSquare = defaultArray

        dynamicArray[0] += 1

        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0

    return generatedLatinSquares
