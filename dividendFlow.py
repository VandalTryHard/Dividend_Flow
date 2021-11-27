"""(RU) Данная программа рассчитывает сумму дивидентов
"""

import pandas as pd
import plotly as pl
import numpy as np
import matplotlib as mp
import csv


def main():
    while True:
        print(f"\n1) Show stocks in portfolio")
        print("2) Add a share")
        print("3) Delete share")
        print("4) Change stock")
        print("5) Select investment interval (in years)")
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


def showStocks():
    df = pd.read_csv("fileStock.csv")
    print(df.head())


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
                        "|Payment once every (days)|": [paymentEvery]}
    fileStock = "fileStock.csv"
    df = pd.DataFrame.from_dict(stockInformation)
    df.to_csv(fileStock, header=False, index=False, mode='a')


# ???????????????????????????????????????????????????????????????????????????????
def deleteShare():
    df = pd.read_csv("fileStock.csv", encoding='utf-8')
    df_np = df.to_numpy()
    print(df_np)
    userChoice = input("Enter Name (ticker): ")
    # column = df['|Name (ticker)|']
    for i in df_np:
        if userChoice in i:
            confirmation = input(f"Are you sure you want to delete {i}? (y/n): ")
            confirmation = confirmation.lower()
            if confirmation == 'y':
                i = True
                print(type(i))
                np.delete(df_np, i)
                print(df_np)
                print("Delete.")
            else:
                print("Not deleted!")
                main()


def changeStock():
    print("changeStock")


def selectInterval():
    print("selectInterval")


def showResults():
    print("showResults")


main()
