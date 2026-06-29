from sklearn.datasets import load_iris # loads iris dataset
from sklearn.neighbors import KNeighborsClassifier # creates KNN  algorithm
import pickle # imports pyhton's built-in library for saving and loading python objects
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# SAVING THE ML MODEL
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")