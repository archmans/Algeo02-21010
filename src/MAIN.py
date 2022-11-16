from operation import *
import numpy as np
from img_processing import *
from covarian import *
from step3EigenAlgo import *
from Mean import *
from AlgoritmaEigen import *

#mengambil himpunan gambar
t = np.array(resize_image(get_image("./test/p"), (256, 256)))
print("\nHimpunan Gambar :\n")
print(t)
print(t.shape)

#mencari nilai mean
mean = Mean(t)
print("\nMean :\n ")
print(mean)

#mencari selisih
selisih = []
for i in range(len(t)):
    selisih.append(KurangMatriks(t[i], mean))
selisih = abs(np.array(selisih))
print("\nSelisih :\n")
print(selisih)
print(selisih.shape)

#mencari covarian
cov = []
for i in range(len(selisih)):
    cov.append(matrix_covarian(selisih[i]))
print("Covarian :\n")
cov = np.array(cov)
print(cov)
print(cov.shape)

#mencari eigen
eigen = []
for i in range(len(cov)):
    Val, Vec = EigenDariQR(cov[i])
    eigen.append(Vec)
eigen = np.array(eigen)
print("\nVector Eigen :\n")
print(eigen)
print(eigen.shape)

#mencari eigen face
eigenFace = []
for i in range(len(eigen)):
    eigenFace.append(KaliMatriks(eigen[i], selisih[i]))
eigenFace = np.array(eigenFace)
print("\nEigen Face :\n")
printMatriks(eigenFace)
print(eigenFace.shape)