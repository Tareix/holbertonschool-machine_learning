#!/usr/bin/env python3
"""Module for loading a CSV file into a Pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """Load a CSV file into a Pandas DataFrame."""
    return pd.read_csv(filename, sep=delimiter)
