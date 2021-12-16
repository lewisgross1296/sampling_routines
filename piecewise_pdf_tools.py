import numpy as np
import os

def createNormalizedPDF(E_grid,bin_vals,N,type):
    '''
    Accepts an energy grid with N points and bin values evaluated on the lower boundary of
    each energy group, except the last bin_vals entry is the energy evaluated at the highest 
    energy. Checks to see if the distribution is normalized. If not, compute and returns
     bin_vals for a normalized pdf. Works for piecewise constant and piecewise linear distributions
    '''
    area = 0.0
    if(np.size(E_grid)!=N):
        print("The energy grid expected ", N, " points, but the grid size is: ",np.size(E_grid),". Original bin_vals returned")
        return bin_vals
    if(type=='constant'):
        # assumes pdf is piecewise with constant value in each region
        for i in range(0,N-1):
            print(i)
            area += bin_vals[i]*(E_grid[i+1] - E_grid[i])
    elif(type=='linear'):
        # assumes pdf is piecewise linear in each region
        for i in range(0,N-1):
            print(i)
            area += (bin_vals[i]+bin_vals[i+1])*(E_grid[i+1] - E_grid[i])/2
    else:
        print("Type: ",type," not recognized, enter linear or constant. Original bin_vals returned")
        return bin_vals

    # divide bin_vals by normalization factor so that pdf is normalized to one
    print("original area under provided data:",area)
    normalized_bin_vals = bin_vals/area
    return normalized_bin_vals