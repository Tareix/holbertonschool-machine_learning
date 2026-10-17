#!/usr/bin/env python3
"""
Initializes all variables required to calculate the P affinities in t-SNE
"""
import numpy as np


def P_init(X, perplexity):
    """
    A function that initializes variables for t-SNE.

    :param X: numpy.ndarray of shape (n, d) containing the dataset
        to be transformed by t-SNE
        n is the number of data points
        d is the number of dimensions in each point
    :param perplexity: the perplexity that all Gaussian distributions
        should have
    :return: (D, P, betas, H)
        D: numpy.ndarray of shape (n, n) containing the pairwise
        squared distances between data points
        P: numpy.ndarray of shape (n, n) initialized to all zeros
        betas: numpy.ndarray of shape (n, 1) initialized to all ones
        H: Shannon entropy for the given perplexity
    """
    n, d = X.shape

    # Calculate pairwise squared Euclidean distances
    # Using (x - y)^2 = x^2 - 2xy + y^2
    sum_X = np.sum(np.square(X), axis=1)
    D = np.add(np.add(-2 * np.dot(X, X.T), sum_X).T, sum_X)
    np.fill_diagonal(D, 0)

    # Initialize the P affinities
    P = np.zeros((n, n))

    # Calculate Shannon entropy
    H = np.log2(perplexity)

    # Initialize beta values
    betas = np.ones((n, 1))

    return D, P, betas, H
