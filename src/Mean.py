from operation import *
import numpy as np

def Mean (listMatriksGambar):
    matriksHasil = np.mean(listMatriksGambar, axis=0).astype(int)
    return matriksHasil

# t = resize_image(get_image("./test/wow"), (256, 256))
# a = Mean(t)
# print(a)

# t = []
# for i in range(10):
#     t.append([[1,2,3],[4,5,6],[7,8,9]])
#     t.append([[9,8,7],[6,5,4],[3,2,1]])
# print(t)
# a = Mean(t)
# print(a)