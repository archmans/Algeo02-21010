import numpy as np
from operation import *

# matrix = np.array([[1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1]])
def matrix_covarian(matrix):
  selisih = matrix
  con_cov = selisih
  # for i in range(1, len(selisih-1)):
  #   con_cov = concat((con_cov, selisih[i]))
  M = con_cov
  return KaliMatriks(M, TransposeMatriks(M))

# cov = matrix_covarian(matrix)
# printMatriks(cov)