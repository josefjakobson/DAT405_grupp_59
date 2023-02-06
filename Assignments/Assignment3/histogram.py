import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Assignments\Assignment3\Data\data_assignment3.csv")
    
sns.histplot(data=data, x="phi")
    
plt.show()

