import pandas as pd
import numpy as np


def creatingTable():
    table = {"|Name (ticker)|": ['STAG'],
             "|Share value|": [42.8],
             "|Number|": [10],
             "|Last payout %|": [0.28],
             "|Payment once every (days)|": [31],
             "|Investment term|": int, }
    df = pd.DataFrame.from_dict(table)
    print(df.head())
    print(df.dtypes)
    fileStock = "fileStock.csv"
    df.to_csv(fileStock, index=False)


creatingTable()
