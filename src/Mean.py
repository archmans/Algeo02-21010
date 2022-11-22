from operation import *
import cv2
import numpy as np
from img_processing import *
def Mean (listMatriksGambar):
    # matriksHasil = np.zeros((0, 0))
    matriksHasil = listMatriksGambar[0]
    for i in range(1, (len(listMatriksGambar))):
        matriksHasil = (matriksHasil+listMatriksGambar[i])
    print(len(listMatriksGambar))
    return matriksHasil/len(listMatriksGambar)