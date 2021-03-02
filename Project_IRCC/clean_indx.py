import pandas as pd
import numpy as np


def cleaner(df):
    """
    This function is designed specifically to clean the multi-level indexing 
    for a raw dataframe from the IRCC data
    """
    # fill NaN using values from the left column if not NaN
    for i in range(df.shape[0]):
        df.iloc[i] = df.iloc[i].ffill()
    # fill NaN from bot to top
    df = df.fillna(method='bfill')
    # create tuples for multi-level index
    tuples = list(zip(*(np.array(df[df.columns[0:4]]).T.tolist())))
    index = pd.MultiIndex.from_tuples(
        tuples, names=["Country", "Program_Lv1", "Program_Lv2", "Program_Lv3"])

    df.index = index
    if df.shape[1] == 106:  # prevent removing columns more than once
        df = df[df.columns[4:]]

    return df
