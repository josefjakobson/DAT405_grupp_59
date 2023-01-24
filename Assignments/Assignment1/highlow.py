import pandas as pd

data = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
mean_Life = data["Life_expectancy"].mean()
mean_GDP = data["GDP (output, multiple price benchmarks)"].mean()
condition_low_life = data['Life_expectancy'] < mean_Life
condition_high_gpd = data["GDP (output, multiple price benchmarks)"] > mean_GDP
condition_high_life = data['Life_expectancy'] > mean_Life
condition_low_gpd = data["GDP (output, multiple price benchmarks)"] < mean_GDP


combined = condition_low_life & condition_high_gpd
resulted_Countries = data.loc[combined]
for country in resulted_Countries["Entity"]:
        # locates all entries where life expectancy was higher than the mean and
        # GDP lower than the mean
        print(country)
