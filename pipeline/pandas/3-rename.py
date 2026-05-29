#!/usr/bin/env python3
"""Module for renaming and formatting stock data."""

import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime and return Datetime and Close."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
