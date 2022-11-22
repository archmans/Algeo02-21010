from operation import *
import numpy as np
from img_processing import *
from covarian import *
from Mean import *
from AlgoritmaEigen import *
import cv2 as cv2

def dataset_processing(folder_path): 
    #mengambil himpunan gambar
    t = np.array(resize_image(get_image(folder_path), (256, 256)))
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
    selisihGabungan = np.array(selisihGabungan)
    print("\nSelisih Gabungan :\n")
    print(selisihGabungan)
    print(selisihGabungan.shape)

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
    return eigenFace, mean, EigenVec, t

def image_processing(image_path, mean, eigenFace, EigenVec, t):
    phototest=cv2.resize(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), (256, 256))
    substest=KurangMatriks(phototest,mean)
    tempresult=KaliMatriks(EigenVec,substest)
    lock = []
    for i in range(len(eigenFace)):
        eigenFace[i]=eigenFace[i]-tempresult
        lock.append(normalized(eigenFace[i]))
    temp = np.empty((256,256))
    min=lock[0]
    max = lock[0]
    temp=eigenFace[0]
    target = 0
    for i in range(len(lock)):
        if min>lock[i]:
            min=lock[i]
            temp=eigenFace[i]
            target=i
        if max<lock[i]:
            max=lock[i]

    print("minimum = ",min)
    print("maximum = ",max)
    a = max-min
    print("a = ",a)
    persentage = (a/max)*100
    persentage = round(persentage, 2)
    treshold = 0.8 * max
    print("persentase = ",persentage,"%")

    print("\nEigen Face :\n")
    print(temp)
    print(temp.shape)
    return t[target], persentage, treshold, min