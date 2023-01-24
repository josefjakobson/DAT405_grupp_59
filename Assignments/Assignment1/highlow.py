import pandas as pd

data = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
mean_Life = data["Life_expectancy"].mean()
mean_GDP = data["GDP (output, multiple price benchmarks)"].mean()
condition_high_gpd = data["GDP (output, multiple price benchmarks)"] > mean_GDP
condition_high_life = data['Life_expectancy'] > mean_Life
condition_low_gpd = data["GDP (output, multiple price benchmarks)"] < mean_GDP

def get_countries(condition):
    resulted_Countries = data.loc[condition]
    for country in resulted_Countries["Entity"]:
        # locates all entries where life expectancy was higher than the mean and
        # GDP lower than the mean
        print(country)

print("High Life, Low GDP")
high_life_and_low_gdp = condition_high_life & condition_low_gpd
get_countries(high_life_and_low_gdp)

print("High Life, High GDP")
high_life_and_high_gdp = condition_high_life & condition_high_gpd
get_countries(high_life_and_high_gdp)

