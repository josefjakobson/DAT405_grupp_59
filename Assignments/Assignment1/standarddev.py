import pandas as pd

data = pd.read_csv("Assignments\Assignment1\Data\merged_data.csv")
sd = data["Life_expectancy"].std()
mean = data["Life_expectancy"].mean()

