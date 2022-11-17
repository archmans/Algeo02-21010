from operation import *
import numpy as np
from img_processing import *
from covarian import *
from step3EigenAlgo import *
from Mean import *
from AlgoritmaEigen import *
import cv2 as cv2

#mengambil himpunan gambar
t = np.array(resize_image(get_image("./test/p"), (256, 256)))
print("\nHimpunan Gambar :\n")
print(t)
print(t.shape)

#mencari nilai mean
mean = Mean(t)
print("\nMean :\n ")
print(mean)
print(mean.shape)

#mencari selisih
selisih = []
for i in range(len(t)):
    selisih.append(KurangMatriks(t[i], mean))
selisih = abs(np.array(selisih))
print("\nSelisih :\n")
print(selisih)
print(selisih.shape)

selisihGabungan = concatAllImage(selisih)

#mencari covarian
cov = matrix_covarian(selisihGabungan)
print("\nCovarian :\n")
print(cov)
print(cov.shape)

#mencari eigen
EigenVal, EigenVec = EigenDariQR(cov)
print("\nVector Eigen :\n")
print(EigenVec)
print(EigenVec.shape)

#mencari eigen face
eigenFace = []
for i in range(len(selisih)):
    eigenFace.append(KaliMatriks(EigenVec, selisih[i]))
eigenFace = np.array(eigenFace)
print("\nEigen Face :\n")
print(eigenFace)
print(eigenFace.shape)
for i in range(len(eigenFace)):
    cv2.imshow('image',eigenFace[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()