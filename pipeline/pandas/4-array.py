#!/usr/bin/env python3
"""Module for converting DataFrame columns to a NumPy array."""

import pandas as pd


def array(df):
    """Return the last 10 rows of High and Close as a NumPy array."""
    return df[['High', 'Close']].tail(10).to_numpy()
