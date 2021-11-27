import pandas as pd


def creatingTable():
    table = {"|Name (ticker)|": ['STAG'],
             "|Share value|": [42.8],
             "|Number|": [10],
             "|Last payout %|": [0.28],
             "|Payment once every (days)|": [31], }
    df = pd.DataFrame.from_dict(table)
    print(df.head())
    print(df.dtypes)
    fileStock = "fileStock.csv"
    df.to_csv(fileStock, index=False)


creatingTable()
