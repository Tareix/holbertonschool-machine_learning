#!/usr/bin/env python3
"""
Calculates a correlation matrix.
"""
import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix from a covariance matrix.

    Args:
        C: numpy.ndarray of shape (d, d) containing a covariance matrix

    Returns:
        numpy.ndarray of shape (d, d) containing the correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    v = np.diag(C)

    # std = [sigma1, sigma2, ..., sigmad]
    std = np.sqrt(v)

    outer_std = np.outer(std, std)

    # Korrelyasiya = Covariance / (sigma_i * sigma_j)
    corr = C / outer_std

    return corr
