import merge
import Scatter
import trim_csv_data

gdp_csv = "Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv"
life_expectancy_csv = "Assignments\Assignment1\Data\life-expectancy.csv"
merged = "Assignments\Assignment1\Data\merged_data.csv"

def start():
    merge.init(gdp_csv, life_expectancy_csv)
    Scatter.init(merged)

start()