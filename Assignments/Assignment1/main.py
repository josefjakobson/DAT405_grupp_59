import merge
import Scatter
import trim_csv_data

gdp_csv = "Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv"
life_expectancy_csv = "Assignments\Assignment1\Data\life-expectancy.csv"
gdp_total_csv = "Assignments\Assignment1\Data\\national-gdp.csv"
merged = "Assignments\Assignment1\Data\merged_data.csv"

def start():
    trim_csv_data.main(gdp_total_csv)
    merge.init(gdp_csv, life_expectancy_csv)
    trim_csv_data.equalize(merged, gdp_total_csv)
    merge.init(gdp_total_csv, merged)
    Scatter.init(merged)

start()