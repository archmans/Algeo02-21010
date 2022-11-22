import numpy as np
import cv2

# matriks[0] kolom

def JumlahMatriks (matriksGambar1, matriksGambar2):
    return np.add(matriksGambar1, matriksGambar2)

def KurangMatriks (matriksGambar1, matriksGambar2):
    return np.subtract(matriksGambar1, matriksGambar2)

def KaliMatriks (matriksGambar1, matriksGambar2):
    matrikshasil = np.dot(matriksGambar1, matriksGambar2)
    return matrikshasil

def TransposeMatriks (matriksGambar):
    matrikshasil = np.transpose(matriksGambar)
    return matrikshasil

def printMatriks (matriksGambar):
    for i in range(len(matriksGambar)):
        for j in range(len(matriksGambar[0])):
            print(matriksGambar[i][j], end=" ")
        print("")

def concat(matriksGambar1, matriksGambar2):
    matrikshasil = np.concatenate((matriksGambar1, matriksGambar2), axis=1)
    return matrikshasil

def concatAllImage(himpunanGambar):
    Con = []
    for i in range(len(himpunanGambar)):
        if i == 0:
            Con = himpunanGambar[i]
        else:
            Con = concat(Con, himpunanGambar[i])
    return Con

def getMinIndex(list):
    min = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            index = i
    return (index, min)

def normalized(matrix):
    jumlahKuadrat = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            jumlahKuadrat += matrix[i][j]**2
    return jumlahKuadrat**(1/2)

def normalizedArray(array):
    jumlahKuadrat = 0
    for i in range(len(array)):
        jumlahKuadrat += array[i]**2
    return jumlahKuadrat**(1/2)

