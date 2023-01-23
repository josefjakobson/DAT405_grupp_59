import pandas as pd
import matplotlib.pyplot as plt

def init(csv):
    scatterPlot(csv)


def scatterPlot(csvfile): #Plots the data as a scatter graph with GDP per capita on the x-axis and life expectancy on the y-axis
    data = pd.read_csv(csvfile)
    
    plt.scatter(data["GDP per capita (constant 2015 US$)"], data["Life_expectancy"], marker=".")
    plt.xlabel("GPD per Capita in USD")
    plt.ylabel("Life Expectancy in years")
    plt.title("Life Expectancy vs GPD per capita in 2019")
    
    plt.show()



