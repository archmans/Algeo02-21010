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

phototest=cv2.resize(cv2.imread("./test/wow/Adriana Lima48_169.jpg", cv2.IMREAD_GRAYSCALE), (256, 256))
substest=KurangMatriks(phototest,mean)
tempresult=KaliMatriks(EigenVec,substest)
lock = []
for i in range(len(eigenFace)):
    eigenFace[i]=eigenFace[i]-tempresult
    lock.append(np.linalg.norm(eigenFace[i]))
temp = np.empty((256,256))
min=lock[0]
temp=eigenFace[0]
target = 0
for i in range(len(lock)):
    if min>lock[i]:
        min=lock[i]
        temp=eigenFace[i]
        target=i

print("\nEigen Face :\n")
print(temp)
print(temp.shape)
cv2.imshow('image',t[target])
cv2.waitKey(0)
cv2.destroyAllWindows()