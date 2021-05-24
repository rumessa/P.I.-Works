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

# calculate the maximum path of the matrix
def calculateSum(matrix, matrixSize):
    # make all primary numbers in our matrix zero
    deletePrimeNumbers(matrix, matrixSize)

    # add row 0 to both numbers in row 1 as row 0 only has 1 number. 
    matrix[1][0] += matrix[0][0]
    matrix[1][1] += matrix[0][0]

    # since row 0 and row 1 already walked over, we now start from row 2
    for row in range(2, matrixSize):
        # add the first element of row - 1 to first element of current row (down) 
        # and add the last element of row - 1 to last element of current row (diagonal)
        matrix[row][0] += matrix[row - 1][0]
        matrix[row][row] += matrix[row - 1][row - 1]
        
        # for all the elements in the middle of row (excluding first and last element) 
        # that can be accessed by both sides of the upper level row elements
        for col in range(1, row):
            down = matrix[row][col] + matrix[row - 1][col]        # check down from row - 1 
            diag = matrix[row][col] + matrix[row - 1][col - 1]    # check diagonal from row -1 
            
            matrix[row][col] = max(down, diag)                    # whichever one results greater sum gets substituted into the position
            
            print(matrix)
    
    # final sum will be in the last row of matrix
    sum = 0
    for col in range(0, matrixSize):
        if matrix[matrixSize - 1][col] > sum:
            sum = matrix[matrixSize - 1][col]
    return sum

            
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

        sum = calculateSum(matrix, matrixSize)
        print("The sum is: {0}".format(sum))
    
    else:
        print("Triangle is too small.")

if __name__ == "__main__":
    main(input("Enter file name please: "))
