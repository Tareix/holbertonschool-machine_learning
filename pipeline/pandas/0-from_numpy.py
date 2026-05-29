#!/usr/bin/env python3
"""Module for creating a Pandas DataFrame from a NumPy array."""

import pandas as pd


def from_numpy(array):
    """Create a DataFrame from a NumPy array."""
    num_cols = array.shape[1]
    columns = [chr(65 + i) for i in range(num_cols)]
    return pd.DataFrame(array, columns=columns)
