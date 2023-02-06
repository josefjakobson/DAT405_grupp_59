import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Assignments\Assignment3\Data\data_assignment3.csv")
    
sns.scatterplot(data=data, x="phi", y="psi", s=3)
    
plt.show()



