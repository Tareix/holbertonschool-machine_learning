#!/usr/bin/env python3
"""Module for setting the DataFrame index."""


def index(df):
    """Set Timestamp as the index and return the DataFrame."""
    return df.set_index('Timestamp')
