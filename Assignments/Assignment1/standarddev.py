import pandas as pd
data = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
sd = data["Life_expectancy"].std()
mean = data["Life_expectancy"].mean()
for elem in data.loc[data['Life_expectancy'] > mean + sd]["Entity"]:
    # locates all entries where life expectancy was higher than one 
    #standard deviation above the mean
    print(elem)
