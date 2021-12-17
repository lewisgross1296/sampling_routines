import piecewise_pdf_tools as pdft
import numpy as np
import matplotlib

# SET UP EXAMPLE PDFS
# piecewise constant
# energy grid given in order from lowest energy to highest energy
E_GRID = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
# value at each energy grid point
BIN_VALS = np.array([1, 5, 4, 2, 2])
# number of energy grid points
N = 5
CONSTANT_NORMALIZED_BIN_VALS = pdft.createNormalizedPDF(E_GRID, BIN_VALS, N, "constant")
print("original bin vals:", BIN_VALS, "returned bin vals:", CONSTANT_NORMALIZED_BIN_VALS)
print('\n')
CONSTANT_NORMALIZED_BIN_VALS_CHECK = pdft.createNormalizedPDF(E_GRID, CONSTANT_NORMALIZED_BIN_VALS , N, "constant")
print('\n')

# piecewise linear
# energy grid given in order from lowest energy to highest energy
E_GRID = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
# value at each energy grid point
BIN_VALS = np.array([1, 5, 3, 2, 6])
# number of energy grid points
N = 5
LINEAR_NORMALIZED_BIN_VALS = pdft.createNormalizedPDF(E_GRID, BIN_VALS, N, "linear")
print("original bin vals:", BIN_VALS, "returned bin vals:", LINEAR_NORMALIZED_BIN_VALS)
print("\n")
LINEAR_NORMALIZED_BIN_VALS_CHECK = pdft.createNormalizedPDF(E_GRID, LINEAR_NORMALIZED_BIN_VALS, N, "linear")
print("\n")

# test what happens when type passed is not constant or linear
FAILED_NORMALIZED_BIN_VALS = pdft.createNormalizedPDF(E_GRID, BIN_VALS, N, "YOLO")
print("original bin vals:", BIN_VALS, "returned bin vals:", FAILED_NORMALIZED_BIN_VALS)


# SET UP EXAMPLE CDFS
