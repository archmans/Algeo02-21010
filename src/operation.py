import numpy as np
import cv2

# matriks[0] kolom

def JumlahMatriks (matriksGambar1, matriksGambar2):
    for i in range(len(matriksGambar1)):
        for j in range(len(matriksGambar1[0])):
            matriksGambar1[i][j] += matriksGambar2[i][j]
    return matriksGambar1

def KurangMatriks (matriksGambar1, matriksGambar2):
    for i in range(len(matriksGambar1)):
        for j in range(len(matriksGambar1[0])):
            matriksGambar1[i][j] -= matriksGambar2[i][j]
    return matriksGambar1

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

# Driver
# satu = [[0 for i in range(3)] for j in range(3)]
# dua = [[0 for i in range(3)] for j in range(3)]

# for i in range(3):
#     for j in range(3):
#         satu[i][j] = i+j
#         dua[i][j] = i-j

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