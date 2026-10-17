#!/usr/bin/env python3
"""
Performs PCA on a dataset
"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d)
        var: fraction of variance to maintain

    Returns:
        W: weights matrix maintaining the required variance
    """
    u, s, vh = np.linalg.svd(X)
    cum = np.cumsum(s)
    thresh = cum[-1] * var
    mask = np.where(thresh > cum)
    selected = cum[mask]
    idx = len(selected) + 1
    W = vh.T
    Wr = W[:, :idx]
    return Wr
