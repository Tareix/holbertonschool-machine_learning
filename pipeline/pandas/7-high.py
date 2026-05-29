#!/usr/bin/env python3
"""Module for sorting a DataFrame by the High column."""


def high(df):
    """Return the DataFrame sorted by High in descending order."""
    return df.sort_values(by='High', ascending=False)
