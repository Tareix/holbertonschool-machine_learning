#!/usr/bin/env python3

import numpy as np

import pandas as pd

def from_numpy(array):
    
    num_cols = array.shape(1)
    columns = [chr(65 + i) for i in range(num_cols)]
    return pd.DataFrame(array, columns=columns)
