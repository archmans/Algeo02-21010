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

def concatBawah(matriksGambar1, matriksGambar2):
    matrikshasil = np.concatenate((matriksGambar1, matriksGambar2), axis=0)
    return matrikshasil

def concatAllImage(himpunanGambar):
    Con = []
    for i in range(len(himpunanGambar)):
        if i == 0:
            Con = himpunanGambar[i]
        else:
            Con = concat(Con, himpunanGambar[i])
    return Con

def concatAllImageBawah(himpunanGambar):
    Con = []
    for i in range(len(himpunanGambar)):
        if i == 0:
            Con = himpunanGambar[i]
        else:
            Con = concatBawah(Con, himpunanGambar[i])
    return Con

def flattenImage(himpunanGambar):
    Con = []
    for i in range(len(himpunanGambar)):
        if i == 0:
            Con = np.ravel(himpunanGambar[i])
        else:
            a = np.ravel(himpunanGambar[i])
            Con = np.r_[Con,a] 
    Con = np.reshape(Con,(len(himpunanGambar),256*256))
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

# # Driver
# satu = [[0 for i in range(3)] for j in range(3)]
# dua = [[0 for i in range(3)] for j in range(3)]

# for i in range(3):
#     for j in range(3):
#         satu[i][j] = i+j
#         dua[i][j] = i-j

# selisih = [[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]],[[0,0,0],[0,0,0],[0,0,0]]]
# a = concatAllImage(selisih)
# print(a)

# print("\nMatriks 1")
# printMatriks(satu)
# print("\nMatriks 2")
# printMatriks(dua)
# print("\njumlah")
# printMatriks(JumlahMatriks(satu, dua))
# print("\nkurang")
# printMatriks(KurangMatriks(satu, dua))
# print("\nkali")
# printMatriks(KaliMatriks(satu, dua))
# print("\ntranspose")
# printMatriks(TransposeMatriks(satu))
# a = concat(satu, dua)
# printMatriks(a)