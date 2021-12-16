import piecewise_pdf_tools as pdft
import matplotlib


# SET UP EXAMPLE PDFS
# piecewise constant
# energy grid given in order from lowest energy to highest energy
E_grid = [0.0,0.25,0.5,0.75,1.0]
# value at each energy grid point
bin_vals = [1,5,3,2,2]
# number of energy grid points 
# TODO this may be unnecessary, 
# may be better practice to compute this N in creatNormalizedPDF
N = 5
normalized_bin_vals = pdft.createNormalizedPDF(E_grid,bin_vals,N,"constant")


# piecewise linear
# energy grid given in order from lowest energy to highest energy
E_grid = [0.0,0.25,0.5,0.75,1.0]
# value at each energy grid point
bin_vals = [1,5,3,2,6]
# number of energy grid points 
# TODO this may be unnecessary, 
# may be better practice to compute this N in creatNormalizedPDF
N = 5
normalized_bin_vals = pdft.createNormalizedPDF(E_grid,bin_vals,N,"linear")


# test what happens when type passed is not constant or linear
normalized_bin_vals = pdft.createNormalizedPDF(E_grid,bin_vals,N,"YOLO")