#!/usr/bin/env python3
"""Module for flipping and transposing a DataFrame."""


def flip_switch(df):
    """Return the DataFrame reversed and transposed."""
    return df.iloc[::-1].T
