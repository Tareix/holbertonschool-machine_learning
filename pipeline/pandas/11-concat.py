#!/usr/bin/env python3
"""Module for concatenating indexed DataFrames."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate two DataFrames with labeled keys."""
    df1_indexed = index(df1)
    df2_indexed = index(df2)
    df2_filtered = df2_indexed.loc[:1417411920]
    return pd.concat(
        [df2_filtered, df1_indexed],
        keys=['bitstamp', 'coinbase']
    )
