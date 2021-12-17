import numpy as np
import os

# OBSOLETE, WORKED ON DURING SW MEETING 12/17, TODO delete after happy with other implementation
def createNormalizedPDF(e_grid, bin_vals, N, type):
    '''
    Accepts an energy grid with N+1 points and bin vals evaluated on the lower boundary of
    each energy group, except the last bin_vals entry is the energy evaluated at the highest problem
    energy. Checks to see if the distribution is normalized. If not, compute and returns
    bin_vals for a normalized pdf. Works for piecewise constant and piecewise linear distributions
    '''
    area = 0.0
    if np.size(e_grid) != N:
        print("The energy grid expected ", N, " points, but the grid size is: ", np.size(
            e_grid), ". Original bin_vals returned")
        return bin_vals
    if type == 'constant':
        # assumes pdf is piecewise with constant value in each region
        area1 = np.dot( bin_vals[:-1],np.array((e_grid[1:]-e_grid[:-1])) ) # call numpy product
        area2 = bin_vals[:-1].dot(e_grid[1:]-e_grid[:-1]) # call dot product from class member function
        # for i in range(0, N-1):
        #     area += bin_vals[i]*(e_grid[i+1] - e_grid[i])
        print("area1: ", area1, "area2: ", area2)
    elif type == 'linear':
        # assumes pdf is piecewise linear in each region
        for i in range(0, N-1):
            area += (bin_vals[i]+bin_vals[i+1])*(e_grid[i+1] - e_grid[i])/2
    else:
        print("type: ", type,
              " unrecognized, enter linear or constant. Original bin_vals returned")
        return bin_vals

    # divide bin_vals by normalization factor so that pdf is normalized to one
    print("original area under provided data:", area)
    normalized_bin_vals = bin_vals/area1
    return normalized_bin_vals

# TODO make more pythonic like other example
def computeCumulativeDensities(e_grid, bin_vals, N, type):
    '''
    Accepts an energy grid with the pdf evaluated at the grid points. Normalizes the distribution 
    in case that it is not normalized. Computes the cumulative density at each rid point and returns 
    this list of cumulative densities
    '''
    normalized_bin_vals = createNormalizedPDF(e_grid, bin_vals, N, type)
    cumulative_vals = np.zeros(N, float)
    if np.size(e_grid) != N:
        print("The energy grid expected ", N, " points, but the grid size is: ", np.size(
            e_grid), ". Original bin_vals returned")
        return cumulative_vals
    if type == 'constant':
        # assumes pdf is piecewise with constant value in each region
        for i in range(0, N):
            cumulative_vals[i+1] = cumulative_vals[i] + \
                (e_grid[i+1] - e_grid[i])*normalized_bin_vals[i]
    elif type == 'linear':
        # assumes pdf is piecewise linear in each region
        for i in range(0, N-1):
            cumulative_vals[i+1] += (normalized_bin_vals[i] +
                                     normalized_bin_vals[i+1])*(e_grid[i+1] - e_grid[i])/2
    else:
        print("type: ", type,
              " not recognized, enter linear or constant. normalized_bin_vals returned")
        return  # TODO what is this appropriate?

    # TODO what is the best way to check for normalization and what to return if not normalized
    # possible check for normalization or other checks
    # if np.isclose(1.0, cumulative_vals[-1], rtol=0.0000001) else cumulative_vals
    return cumulative_vals


def createNormalizedPDF(e_grid, bin_vals):
    '''
    #TODO add docstring
    '''
    area = 0.0
    n_e = np.size(e_grid)
    n_b = np.size(bin_vals)
    # piecewise linear since there are as many bin vals as grid points
    if n_e == n_b:
        uppers = bin_vals[1:]
        lowers = bin_vals[:-1]
        mean_heights = (uppers + lowers) / 2
        area = np.dot(mean_heights,np.array(e_grid[1:]-e_grid[:-1]))
    # piecewise constant since there is one more grid point than bin vals
    if n_e == n_b+1:
        mean_heights = bin_vals
        area = np.dot(mean_heights,np.array(e_grid[1:]-e_grid[:-1]))
    else:
        print("The difference bewtween the sizes of the grid and values was not 0 or 1, format incorrect")
    normalized_bin_vals = bin_vals/area
    return normalized_bin_vals

def computeCumulativeDensities(e_grid, bin_vals):
    '''
    #TODO add docstring
    '''
    normalized_bin_vals = createNormalizedPDF(e_grid, bin_vals)
    n_e = np.size(e_grid)
    n_b = np.size(bin_vals)
    cumulative_vals = np.zeros(n_e, float)
    # pythonic way to get the area at each grid point without a loop...
    return cumulative_vals


# def invertCDF(e_grid,cumulative_vals)
