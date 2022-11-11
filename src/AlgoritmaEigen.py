import numpy as np
import sympy as sy
from sympy import * # type: ignore

def printMatriks (matriksGambar):
    for i in range(len(matriksGambar)):
        for j in range(len(matriksGambar[0])):
            print(matriksGambar[i][j], end=" ")
        print()

def matriksLamda(matrix,n):
    lamda = symbols('λ')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                matrix[i][j] = (lamda - matrix[i][j])
            else:
                matrix[i][j] *= -1
    return matrix

def determinanMatriks(matrix):
    matrix = Matrix(matrix)
    determinan = matrix.det()
    return determinan
    
def cariAkarAkar(determinan):
    faktor = solve(determinan)
    return faktor

def getEigenValue(matrix,n):
    matrix = matriksLamda(matrix,n)
    determinan = determinanMatriks(matrix)
    eigenValue = cariAkarAkar(determinan)
    return eigenValue

