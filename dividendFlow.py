"""(RU) Данная программа рассчитывает сумму дивидентов
"""
import matplotlib.pyplot as plt
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
    import math
    today = dt.today().strftime('%d/%m/%y')
    value_Share = float(df["|Share value|"][1])
    numbers = int(df["|Number|"][1])
    payout_Last = float(df["|Last payout %|"][1])
    payment_once_every = int(df["|Payment once every (days)|"][1])
    term_Inv = int(df["|Investment term|"][1])

    terms = []
    for t in range(0, term_Inv):
        terms.append(t)

    payments = []
    for p in range(0, term_Inv):
        p = float(p / payment_once_every)
        payments.append(p)

    values = []
    for v in range(0, term_Inv):
        v = float((((value_Share * numbers) * payout_Last / 100) * 70) / 100)  # с учетом налога так как недвига
        values.append(v)

    value = []
    for v in values:
        # реализовать изменение дохода от времени!!!!!!!!!!!!

    x = terms
    y = value
    plt.plot(x, y)
    plt.show()

    # violate = (value_Share*numbers)*payout_Last/100
    # term =
    # print(violate)
    # x = np.arange(0, 1, 1)
    # y = np.arange(0, violate, 0.5)
    # plt.plot(x, y)
    # plt.xlabel("angle")
    # plt.ylabel("sine")
    # plt.title('sine wave')
    # plt.show()

    # for i in range(0, term_Inv):
    #     x = i + 1
    #     y = value_Share
    #     x, y = [x, y]
    #     mp.show(x, y)


main()
