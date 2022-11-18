# import numpy as np
# import sympy as sy
# from sympy import * # type: ignore
# from operation import concat

import numpy as np
import operation as op
from img_processing import *


# def DekomposisiQR(matrix):
#     m, n = matrix.shape
#     Q = np.zeros((m, n))
#     R = np.zeros((n, n))
#     for j in range(n):
#         v = matrix[:, j]
#         for i in range(j - 1):
#             q = Q[:, i]
#             R[i, j] = q @ v
#             v = v - R[i, j] * q
#         norm = np.linalg.norm(v)
#         Q[:, j] = v / norm
#         R[j, j] = norm
#     return Q, R

def DekomposisiQR(matrix):
    m, n = matrix.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        k = matrix[:, j]
        for i in range(j - 1):
            l = Q[:, i]
            R[i, j] = l @ k
            k = k - R[i, j] * l
        norm = np.linalg.norm(k)
        Q[:, j] = k / norm
        R[j, j] = norm
    return Q, R

def EigenDariQR(matrix):
    PQ = np.eye(matrix.shape[0])
    copy=matrix.copy()
    for i in range(1):
            Q,R = DekomposisiQR(copy)
            PQ = PQ @ Q;
            copy = R @ Q;
    EigenVal = np.diag(copy)
    EigenVec = PQ
    return EigenVal, EigenVec


# # driver
# t = 0000
# print(t)
# print(t.shape)
# g = np.array(t)
# print(np.linalg.eig(g)[0])

# c, d = EigenDariQR(t)
# # print("\nvalue\n")
# # print(c)
# # print(len(c))
# print("\nvector\n")  
# print(d)
# print(d.shape)
