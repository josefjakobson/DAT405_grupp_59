import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


# import some data to play with
iris = datasets.load_iris()

# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Create color maps
cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
cmap_bold = ["darkorange", "c", "darkblue"]

for weights in ["uniform", "distance"]:
    for k in range(1, 101, 10):
        # we create an instance of Neighbours Classifier and fit the data.
        knn = neighbors.KNeighborsClassifier(k, weights=weights).fit(X, y)
        # Plot also the training points
        print(weights, ": ", knn.score(X_train, y_train), "\n")
        y_pred = knn.predict(X_test)
        knn_conf_mat = confusion_matrix(y_test, y_pred)
        print(f"Confusion Matrix with weight {weights} and k = {k}: \n", knn_conf_mat)
        class_report = classification_report(y_test, y_pred)
        print(f"\nClassification Report with weight {weights} and k = {k}: \n", class_report)


plt.show()
