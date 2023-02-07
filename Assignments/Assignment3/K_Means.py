import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

intertia_list = []
k_list = []

data = pd.read_csv("Assignments\Assignment3\Data\data_assignment3.csv")

df = pd.DataFrame(data, columns=['psi','phi'])

for i in range(1,9):
    KM = KMeans(n_clusters=i).fit(df)
    intertia_list.append(KM.inertia_)
    k_list.append(i)

#plt.scatter(df['phi'], df['psi'], c=KM.labels_.astype(float))
#plt.show()

plt.plot(k_list, intertia_list)
plt.title('Elbow method')
plt.xlabel('K')
plt.ylabel('Diameter')
plt.show()


