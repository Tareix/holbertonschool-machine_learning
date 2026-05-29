#!/usr/bin/env python3
"""Module for concatenating DataFrames with a hierarchical index."""

import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate bitstamp and coinbase data using a MultiIndex."""
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    df = pd.concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )

    return df.swaplevel().sort_index()
