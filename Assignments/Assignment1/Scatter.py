import pandas as pd
import matplotlib.pyplot as plt

def init():
    csvfile1 = "Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv"
    csvfile2 = "Assignments\Assignment1\Data\life-expectancy.csv"
    return csvfile1, csvfile2


def scatterPlot(csvfile1, csvfile2):
    dfGDP = pd.read_csv(csvfile1)
    dfLifeExpectancy = pd.read_csv(csvfile2)



    for col in dfGDP.columns:
        plt.scatter(dfGDP[col], dfLifeExpectancy[col], label= "GDP per capita vs. Life expectancy Worldwise 2019")
    plt.legend(loc='best', fontsize=16)
    plt.xlabel('Life expectancy')
    plt.ylabel('GDP per capita')



csvfile1, csvfile2 = init()
scatterPlot(csvfile1, csvfile2)

