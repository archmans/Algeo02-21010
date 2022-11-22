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


# t = resize_image(get_image("./test/wow"), (256, 256))
# a = Mean(t)
# cv2.imshow('image',a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(a)

# t = []
# for i in range(10):
#     t.append([[1,2,3],[4,5,6],[7,8,9]])
#     t.append([[9,8,7],[6,5,4],[3,2,1]])
# print(t)
# a = Mean(t)
# print(a)