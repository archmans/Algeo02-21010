import numpy as np
from operation import *
matrix = np.array([[1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1]])
def matrix_covarian(matrix):
  return KaliMatriks(matrix, TransposeMatriks(matrix))

cov = matrix_covarian(matrix)
printMatriks(cov)