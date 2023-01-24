import pandas as pd

data = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
mean_Life = data["Life_expectancy"].mean()
mean_GDP = data["GDP (output, multiple price benchmarks)"].mean()
mean_GDP_per_capita = data["GDP per capita (constant 2015 US$)"].mean()
high_gdp = data["GDP (output, multiple price benchmarks)"] > mean_GDP
high_life = data['Life_expectancy'] > mean_Life
low_gpd = data["GDP (output, multiple price benchmarks)"] < mean_GDP
high_gdp_per_capita = data["GDP per capita (constant 2015 US$)"] > mean_GDP_per_capita




#here are all conditions. they all have high life expectancy
low_gdp_condition = high_life & low_gpd
high_gdp_condition = high_life & high_gdp
high_gdp_per_capita_condition = high_life & high_gdp_per_capita

def get_countries(condition):
    resulted_Countries = data.loc[condition]
    for country in resulted_Countries["Entity"]:
        # locates all entries for a certain condition
        print(country)

print("High Life, Low GDP")
get_countries(low_gdp_condition)

print("High Life, High GDP")
get_countries(high_gdp_condition)

print("High Life, High GDP per capita")
get_countries(high_gdp_per_capita)