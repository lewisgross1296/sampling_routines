import numpy as np
import os

def createNormalizedPDF(E_GRID, BIN_VALS , N, TYPE):
    '''
    Accepts an energy grid with N points and bin values evaluated on the lower boundary of
    each energy group, except the last BIN_VALS entry is the energy evaluated at the highest problem
    energy. Checks to see if the distribution is normalized. If not, compute and returns
    BIN_VALS for a normalized pdf. Works for piecewise constant and piecewise linear distributions
    '''
    area = 0.0
    if np.size(E_GRID) != N:
        print("The energy grid expected ", N, " points, but the grid size is: ", np.size(E_GRID), ". Original BIN_VALS returned")
        return BIN_VALS
    if TYPE == 'constant':
        # assumes pdf is piecewise with constant value in each region
        for i in range(0, N-1):
            area += BIN_VALS[i]*(E_GRID[i+1] - E_GRID[i])
    elif TYPE == 'linear':
        # assumes pdf is piecewise linear in each region
        for i in range(0, N-1):
            area += (BIN_VALS[i]+BIN_VALS[i+1])*(E_GRID[i+1] - E_GRID[i])/2
    else:
        print("TYPE: ", TYPE, " unrecognized, enter linear or constant. Original BIN_VALS returned")
        return BIN_VALS

    # divide BIN_VALS by normalization factor so that pdf is normalized to one
    print("original area under provided data:", area)
    normalized_bin_values = BIN_VALS/area
    return normalized_bin_values


def computeCumulativeDensities(E_GRID, BIN_VALUES, N, TYPE):
    normalized_bin_values = createNormalizedPDF(E_GRID, BIN_VALUES, N, TYPE)
    cumulative_values = np.zeros(N, float)
    if np.size(E_GRID) != N:
        print("The energy grid expected ", N, " points, but the grid size is: ", np.size(E_GRID), ". Original BIN_VALS returned")
        return cumulative_values
    if TYPE == 'constant':
        # assumes pdf is piecewise with constant value in each region
        for i in range(0, N):
            cumulative_values[i+1] = cumulative_values[i] + (E_GRID[i+1] - E_GRID[i])*normalized_bin_values[i]
    elif TYPE == 'linear':
        # assumes pdf is piecewise linear in each region
        for i in range(0, N-1):
            cumulative_values[i+1] += (normalized_bin_values[i]+normalized_bin_values[i+1])*(E_GRID[i+1] - E_GRID[i])/2
    else:
        print("TYPE: ", TYPE, " not recognized, enter linear or constant. normalized_bin_values returned")
        return normalized_bin_values #TODO is this appropriate?

    # TODO what is the best way to check for normalization and what to return
    return cumulative_values if np.isclose(1.0, cumulative_values[-1], rtol=0.0000001) else cumulative_values
