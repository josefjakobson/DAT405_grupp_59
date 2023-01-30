from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Loads iris dataset
iris = load_iris()
X = iris.data
y = iris.target


# Splits data into test and training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Creates the regression model
classify = LogisticRegression(max_iter=10000)

# Fit the model to the training data
classify.fit(X_train, y_train)

# Predict the class labels of the test data
y_prediction = classify.predict(X_train)


# Create a confusion matrix
conf_mat = confusion_matrix(y_test, y_prediction)
print("Confusion Matrix: \n", conf_mat)

conf_mat_normalized = confusion_matrix(y_test, y_prediction)
print("Normalized confusion Matrix: \n",True, conf_mat_normalized)

class_report = classification_report(y_test, y_prediction)
print("\nClassification Report: \n", class_report)