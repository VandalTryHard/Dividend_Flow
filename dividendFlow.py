"""(RU) Данная программа рассчитывает сумму дивидентов
"""

import pandas as pd
import plotly as pl
import csv


def main():
    while True:
        print("1) Show stocks in portfolio")
        print("2) Add a share")
        print("3) Delete share")
        print("4) Change stock")
        print("5) Select investment interval (in years)")
        print("6) Show total and graph")
        print("7) Exit")
        user_choice = int(input("Enter: "))
        fileStock = open("fileStock.csv", "a")
        fileStock.close()
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
    print("showStocks")


def addShare():
    print("addShare")


def deleteShare():
    print("deleteShare")


def changeStock():
    print("changeStock")


def selectInterval():
    print("selectInterval")


def showResults():
    print("showResults")


main()
