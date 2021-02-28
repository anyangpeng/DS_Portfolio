import pandas as pd
import matplotlib.pyplot as plt


def multiplot(df):
    """
    This function generates multiple lineplots using a dataframe, 
    each line in the plot represent a row in the dataframe
    """

    rn = df.shape[0]
    for i in range(rn):
        plt.plot(df.columns, df.iloc[i], '-o')
    plt.legend(df.index)
    plt.xticks(rotation=90)
