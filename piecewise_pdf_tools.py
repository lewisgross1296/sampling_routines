import numpy as np
import os


def createNormalizedPDF(e_grid, bin_vals, N, type):
    '''
    Accepts an energy grid with N points and bin values evaluated on the lower boundary of
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
        for i in range(0, N-1):
            area += bin_vals[i]*(e_grid[i+1] - e_grid[i])
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
    normalized_bin_values = bin_vals/area
    return normalized_bin_values


def computeCumulativeDensities(e_grid, BIN_VALUES, N, type):
    normalized_bin_values = createNormalizedPDF(e_grid, BIN_VALUES, N, type)
    cumulative_values = np.zeros(N, float)
    if np.size(e_grid) != N:
        print("The energy grid expected ", N, " points, but the grid size is: ", np.size(
            e_grid), ". Original bin_vals returned")
        return cumulative_values
    if type == 'constant':
        # assumes pdf is piecewise with constant value in each region
        for i in range(0, N):
            cumulative_values[i+1] = cumulative_values[i] + \
                (e_grid[i+1] - e_grid[i])*normalized_bin_values[i]
    elif type == 'linear':
        # assumes pdf is piecewise linear in each region
        for i in range(0, N-1):
            cumulative_values[i+1] += (normalized_bin_values[i] +
                                       normalized_bin_values[i+1])*(e_grid[i+1] - e_grid[i])/2
    else:
        print("type: ", type,
              " not recognized, enter linear or constant. normalized_bin_values returned")
        return normalized_bin_values  # TODO is this appropriate?

    # TODO what is the best way to check for normalization and what to return
    return cumulative_values if np.isclose(1.0, cumulative_values[-1], rtol=0.0000001) else cumulative_values
