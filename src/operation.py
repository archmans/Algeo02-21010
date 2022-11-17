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