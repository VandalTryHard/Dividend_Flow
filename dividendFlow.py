"""(RU) Данная программа рассчитывает сумму дивидентов
"""

import pandas as pd
import plotly as pl
import numpy as np
import matplotlib as mp
import csv
from datetime import datetime as dt

df = pd.read_csv("fileStock.csv")


def main():
    while True:
        print(f"\n1) Show stocks in portfolio")
        print("2) Add a share")
        print("3) Delete share")
        print("4) Change stock")
        print("5) Select investment interval (in days)")
        print("6) Show total and graph")
        print("7) Exit")
        user_choice = int(input("Enter: "))
        if user_choice == 1:
            showStocks()
        elif user_choice == 2:
            addShare()
        elif user_choice == 3:
            deleteShare()
        elif user_choice == 4:
            changeStock()
        elif user_choice == 5:
            selectInterval()
        elif user_choice == 6:
            showResults()
        elif user_choice == 7:
            quit()
        else:
            print("Error try again: ")
            main()


# 1
def showStocks():
    df_view = pd.read_csv("fileStock.csv")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', df_view.shape[0] + 1)
    print(df_view)
    print(df_view.dtypes)


# 2
def addShare():
    nameTicker = input("Name (ticker): ")
    shareValue = float(input("Share value: "))
    number = int(input("Number: "))
    lastPayout = float(input("Last payout (%): "))
    paymentEvery = int(input("Payment once every (days): "))
    stockInformation = {"|Name (ticker)|": [nameTicker],
                        "|Share value|": [shareValue],
                        "|Number|": [number],
                        "|Last payout %|": [lastPayout],
                        "|Payment once every (days)|": [paymentEvery],
                        "|Investment term|": int, }
    fileStock = "fileStock.csv"
    df_add = pd.DataFrame.from_dict(stockInformation)
    df_add.to_csv(fileStock, header=False, index=False, mode='a')


# 3
def deleteShare():
    fileStock_del = csv.reader(open("fileStock.csv"))
    rows = list(fileStock_del)
    userChoice = input("Enter Name (ticker): ")
    for row in rows:
        if userChoice in row:
            confirmation = input(f"Are you sure you want to delete {row}? (y/n): ")
            if confirmation == "y":
                rows.remove(row)
                writer = csv.writer(open("fileStock.csv", "w", newline=""))
                writer.writerows(rows)
                print("Successfully deleted.")
                main()
            else:
                print("Not deleted!")
                main()
    print("Value Error")
    # df = pd.read_csv("fileStock.csv", encoding='utf-8')
    # df_np = df.to_numpy()
    # print(df_np)
    # userChoice = input("Enter Name (ticker): ")
    # # column = df['|Name (ticker)|']
    # for i in df_np:
    #     if userChoice in i:
    #         confirmation = input(f"Are you sure you want to delete {i}? (y/n): ")
    #         confirmation = confirmation.lower()
    #         if confirmation == 'y':
    #             fileStock_del = csv.reader()
    #         else:
    #             print("Not deleted!")
    #             main()


# 4
def changeStock():
    print("changeStock")


# 5
def selectInterval():
    # today = int(dt.today().strftime('%d'))
    fileStock_Interval = csv.reader(open("fileStock.csv"))
    rows = list(fileStock_Interval)
    nameTicker = input("Enter Name (ticker): ")
    for row in rows:
        if nameTicker in row:
            # print(row)
            # print(type(row))
            userInvestmentTerm = input("Enter the investment period (in days): ")
            row[-1] = int(userInvestmentTerm)
            print(f"You invested in {nameTicker} for {userInvestmentTerm} days ")
            # print(type(row[-1]))
            writer = csv.writer(open("fileStock.csv", "w", newline=""))
            writer.writerows(rows)
            # for nameTicker in row:
            #     print(row)
            #     writer = csv.writer(open("fileStock.csv", "w", newline=""))
            #     writer.writerows(rows)


def showResults():
    print("showResults")


main()
