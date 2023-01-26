import pandas as pd

data = pd.read_csv("Assignments\Assignment2\Data\data_assignment2.csv")

data.drop(columns=["Rooms","Land_size","Biarea","Age"], inplace=True)

data.to_csv("Assignments\Assignment2\Data\data_assignment2_trimmed.csv", index=False)