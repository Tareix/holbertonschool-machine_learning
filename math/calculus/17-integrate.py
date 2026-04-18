#!/usr/bin/env python3
"""
Function that computes the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Returns the integral of a polynomial
    """
    if (not isinstance(poly, list) or len(poly) == 0 or
            not all(isinstance(c, (int, float)) for c in poly) or
            not isinstance(C, (int, float))):
        return None

    result = [C]

    for i, coef in enumerate(poly):
        value = coef / (i + 1)
        result.append(value)

    # remove trailing zeros (keep at least one element)
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # convert floats that are whole numbers to int
    for i in range(len(result)):
        if result[i] == int(result[i]):
            result[i] = int(result[i])

    return result
