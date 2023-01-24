import pandas as pd

data_Life = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
data_GDP = pd.read_csv("Assignments\Assignment1\Data\\national-gdp.csv")
mean_Life = data_Life["Life_expectancy"].mean()
mean_GDP = data_GDP["GDP (output, multiple price benchmarks)"].mean()

for elem in data_Life.loc[data_Life ["Life_expectancy"] > mean_Life]:
    if data_GDP.loc[data_GDP ["GDP (output, multiple price benchmarks)"] > mean_GDP]:
# locates all entries where life expectancy was higher than the mean and
# GDP lower than the mean
        print(elem)


