from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


data = pd.read_csv("Assignments\Assignment3\Data\data_assignment3.csv")

pro_data = data[data["residue name"] == "PRO"]

data = pd.DataFrame(pro_data, columns=["phi", "psi"])
clusters = DBSCAN(eps=10, min_samples=4).fit(data)
labels = clusters.labels_
sns.scatterplot(data=data, x="phi", y="psi", hue=labels, palette="deep", legend=False)
plt.show()