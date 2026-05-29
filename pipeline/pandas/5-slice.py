#!/usr/bin/env python3
"""Module for slicing a DataFrame."""

def slice(df):
    """Select specific columns and every 60th row."""
    columns = ['High', 'Low', 'Close', 'Volume_(BTC)']
    return df[columns].iloc[::60]
