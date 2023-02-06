from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


data = pd.read_csv("Assignments\Assignment3\Data\data_assignment3.csv")

data = pd.DataFrame(data, columns=["phi", "psi"])
clusters = DBSCAN(eps=15, min_samples=50).fit(data)
labels = clusters.labels_
p = sns.scatterplot(data=data, x="phi", y="psi", hue=labels, palette="deep", legend=False)

outliers = Counter(labels)[-1] #Calculate number of outliers

print(outliers)

plt.show()
