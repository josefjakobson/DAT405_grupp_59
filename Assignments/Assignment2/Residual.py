import matplotlib.pyplot as plt
import pandas as pd
import get_data
import seaborn 


df = pd.read_csv("Assignments\Assignment2\Data\data_assignment2.csv")

seaborn.residplot(data=df,x="Living_area", y="Selling_price")
plt.show()
