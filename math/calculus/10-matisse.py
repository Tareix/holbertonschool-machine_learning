#!/usr/bin/env python3
"""Calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Function that calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for x in poly:
        if not isinstance(x, (int, float)):
            return None
    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

   while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
