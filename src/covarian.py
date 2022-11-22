import numpy as np
from operation import *

# matrix = np.array([[1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1]])
def matrix_covarian(matrix):
  matrixT = np.transpose(matrix)
  return matrix @ matrixT

# cov = matrix_covarian(matrix)
# printMatriks(cov)