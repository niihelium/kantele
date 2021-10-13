import numpy as np
from math import sqrt

x = np.array([[0, 1],
              [1, 0]])
              
"""
Because I decided to use little endian notation (0 qubit is least significant qubit),
CNOT gate should be written in different form than original:
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0]])
"""
cx = np.array([[1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 1, 0, 0]])

y = np.array([[0, -1j],
              [1j, 0]])

h = np.array([[1, 1],
              [1, -1]]) / sqrt(2)
