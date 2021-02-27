# This script is used to clean VanGogh_palette data

import os
import numpy as np
import pandas as pd


def datacleaner(file):
    """
    This function clean the VanGogh txt file to list of RGB in tuples
    """

    palette = pd.read_csv(file, header=None)
    # Clean data
    palette[0] = palette[0].apply(lambda x: int(x.strip('[').strip('(')))
    palette[2] = palette[2].apply(lambda x: int(x.strip(' ').strip(')')))
    palette[5] = palette[5].apply(lambda x: int(x.strip(')')))
    palette[8] = palette[8].apply(lambda x: int(x.strip(')')))
    palette[11] = palette[11].apply(lambda x: int(x.strip(')')))
    palette[3] = palette[3].apply(lambda x: int(x.strip().strip('(')))
    palette[6] = palette[6].apply(lambda x: int(x.strip().strip('(')))
    palette[9] = palette[9].apply(lambda x: int(x.strip().strip('(')))
    palette[12] = palette[12].apply(lambda x: int(x.strip().strip('(')))
    palette[14] = palette[14].apply(lambda x: int(x.strip(']').strip(')')))

    # Convert to tuple
    rgb = []
    for i in range(palette.shape[0]):
        rgb.append([np.array([palette.iloc[i][0], palette.iloc[i][1], palette.iloc[i][2]]),
                    np.array([palette.iloc[i][3], palette.iloc[i]
                              [4], palette.iloc[i][5]]),
                    np.array([palette.iloc[i][6], palette.iloc[i]
                              [7], palette.iloc[i][8]]),
                    np.array([palette.iloc[i][9], palette.iloc[i]
                              [10], palette.iloc[i][11]]),
                    np.array([palette.iloc[i][12], palette.iloc[i][13], palette.iloc[i][14]])])
    return(rgb)
