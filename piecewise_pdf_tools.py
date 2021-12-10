import numpy
import os,sys

# TO DO make these formulas right for constant or 
def createNormalizedPDF(E_grid,bin_vals,N,type):
    area = 0.0
    if(type=='constant'):
        # assumes pdf is piecewise with constant value in each region
        for i in range(0,N-1):
            print(i)
            area += bin_vals[i]*(E_grid[i+1] - E_grid[i])
    else:
        # assumes pdf is piecewise linear in each region
        for i in range(0,N-1):
            print(i)
            area += (bin_vals[i]+bin_vals[i+1])*(E_grid[i+1] - E_grid[i])/2
    # do stuff to normalize
    nomralized_bin_vals = bin_vals/area
    print(nomralized_bin_vals)
    return normalized_bin_vals