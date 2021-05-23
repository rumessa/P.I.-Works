import os
import math
import sys

# using wilson's theorem to check if prime number or not; if (n-1)! is divisable by n then it is a prime number
def primeNumber(number):
    if number == 0 or number == 1:
        return 0
    else:
        fact = math.factorial(number - 1)
        if (fact + 1) % number == 0:
            return 1
        else:
            return 0

# getting rid of leading spaces in string copied from file
def normalSpaces(s):
    return ' '.join(s.split())

# getting rid of all prime numbers in the matrix by making them zero
def deletePrimeNumbers(matrix, matrixSize):
    for row in range(1, len(matrix)):
        for col in range(len(matrix[row])):
            if primeNumber(matrix[row][col]) == 1:
                matrix[row][col] = 0

# adding trailing zeroes
def addZeroes(matrix, matrixSize):
    zeroAmount = matrixSize - 1
    for subList in matrix:
        count = 0
        while count < zeroAmount:
            subList.append(0)
            count += 1
        zeroAmount -=  1

# calculate the maximum path of the matrix
# looking at the second last row we check for each number the diagonal and down. whichever is bigger we add it to the number.
# we do the same for all as we go up
def calculateSum(matrix, matrixSize):
    for row in range(matrixSize-2, -1, -1):
        for col in range(0, row+1):
            deletePrimeNumbers(matrix, matrixSize)
            matrix[row][col] += max(matrix[row + 1][col], matrix[row + 1][col + 1])
    return matrix[row][col]
            
def main(filename):
    # read the triangle from file and put into a list
    with open(os.path.join(sys.path[0],filename), "r") as myFile:
        data = myFile.readlines()    

    if len(data) > 1: 
        matrix = []
        data = [normalSpaces(sublist) for sublist in data]   # to get rid of spaces in the strings inside data        
            
        # make the list of strings into list of integers
        for line in data:
            subList = list(map(int, line.split()))
            matrix.append(subList)

        matrixSize = len(matrix)

        addZeroes(matrix, matrixSize)    # add zeroes to make proper m x m matrix
        sum = calculateSum(matrix, matrixSize)
        print("The sum is: {0}".format(sum))
    
    else:
        print("Triangle is too small.")

if __name__ == "__main__":
    main(input("Enter file name please: "))