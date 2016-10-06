#!bin/usr/env python3

import numpy as np

"""

"""

def diff_matrix(n,h):
    """
    Parameters
    ----------
        n: int
            Number of sampling points in mesh
        h: float
            Distance between sample points

    Returns
    -------
        f_prime: np.array
            Mesh of points representing the derivative of the function using finite differences
    """
    D = np.zeros((n,n))
    for i in range(1, n-1):
        for j in range(n):
            if i == j - 1:
                D[i][j] = 1 / (h * 2.0)
            elif i == j + 1:
                D[i][j] = -1 / (h * 2.0)
    D[0][0] = -1.0 / h
    D[0][1] = 1.0 / h
    D[n-1][n-2] = -1.0 / h
    D[n-1][n-1] = 1.0 / h
    return D

def int_matrix(n,h):
    """
    Parameters
    ----------
        n: int
            Number of sampling points in mesh
        h: float
            Distance between sample points

    Returns
    -------
        f_prime: np.array
            Mesh of points representing the integral of the function using finite differences
    """
    D = np.zeros((n,n))
    for i in range(1, n-1):
        for j in range(n):
            if i == j - 1:
                D[i][j] = 1 / (h / 2.0)
            elif i == j + 1:
                D[i][j] = 1 / (h / 2.0)
    D[0][0] = 1.0 * h
    D[0][1] = 1.0 * h
    D[n-1][n-2] = 1.0 * h
    D[n-1][n-1] = 1.0 * h
    return D

def int_Squared_matrix(n,h):
    return int_matrix(n,h).dot(int_matrix(n,h))

def diff_Squared_matrix(n,h):
    return diff_matrix(n,h).dot(diff_matrix(n,h))

print(int_matrix(10,1))
print diff_Squared_matrix(10,1)
