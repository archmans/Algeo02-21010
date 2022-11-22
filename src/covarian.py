import numpy as np
from operation import *

def matrix_covarian(matrix):
  matrixT = np.transpose(matrix)
  return matrix @ matrixT