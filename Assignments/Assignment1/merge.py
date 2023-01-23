import pandas as pd

# Merges the two csv-files into one to make it simpler to create a plot. 
# Since both datasets only contain countries that are in both and are ordered alphabetically, this ensures that the life expectancy is 
# correctly paired to their respective countries
data1 = pd.read_csv("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv")
data2 = pd.read_csv("Assignments\Assignment1\Data\life-expectancy.csv")

data1["Life_expectancy"] = data2["Life_expectancy"]

data1.to_csv("Assignments\Assignment1\Data\merged_data.csv", index=False)
