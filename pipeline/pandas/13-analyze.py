#!/usr/bin/env python3
"""Module for generating descriptive statistics."""


def analyze(df):
    """Return descriptive statistics for the DataFrame."""
    return df.drop(columns=['Timestamp']).describe()
