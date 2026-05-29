#!/usr/bin/env python3
"""Module for removing rows with missing Close values."""


def prune(df):
    """Remove rows where Close is missing."""
    return df.dropna(subset=['Close'])
