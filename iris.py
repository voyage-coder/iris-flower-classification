from sklearn.datasets import load_iris # from scikit.learn library import iris dataset
import pandas as pd # for converting iris data into a table like excel
from sklearn.model_selection import train_test_split # a function used to split dataset into training and testing sets
from sklearn.neighbors import KNeighborsClassifier # import model
from sklearn.metrics import accuracy_score # for calculating accuracy of predicted answers

iris = load_iris() # load iris dataset into memeory and store it in iris variable
# iris - data, target, feature_names, target_names, DESCR
# print(iris) -> looks messy
# print(iris.data) -> big list of numbers like each flower = each row and each col = each measurement
# print(iris.target) -> list of target answers
# print(iris.feature_names) -> ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# print(iris.target_names) -> ['setosa' 'versicolor' 'virginica']

df = pd.DataFrame(iris.data, columns=iris.feature_names) # convert iris data into table using DataFrame and give feature names as column names
# print(df.head()) -> preview or print first 5 rows only
# df["target"] = iris.target -> this can be written when you want to visualize whole dataset with flower types

# X -> input features - flower measurements
# y -> target(answer) - flower type classify
# X = df.drop("target", axis = 1) -> if target column added to df
# y = df["target"]
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size = 0.2,
    random_state=42 # this means for every shuffle dataset shuffles same then accuracy same for every run
) # dataset is splitted into 20% test and 80% training data

model = KNeighborsClassifier() # create model -> we can keep (n_neighbors = 1 0r 5 or any number) - this may change accuracy
# load_iris() and KNeighborsClassifier() both creates an object
# Right now the model knows nothing, it is empty, knowledge = 0, it hasn't learned anything

model.fit(X_train, y_train) # important line in beginner ML
# model is the object we created, .fit() means learn from the training data - it literally means fit yourself using X_train and y_train

y_pred = model.predict(X_test) # after training, the model predicts answers for X_test- testing data
# we don't use y_test here because during testing we don't provide answers to the model

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy : ", accuracy)
print("Accuracy Percentage : ", accuracy * 100, "%") # if needed in percentage

sepal_length = float(input("Enter sepal length : "))
sepal_width = float(input("Enter sepal width : "))
petal_length = float(input("Enter petal length : "))
petal_width = float(input("Enter petal width : "))
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(new_flower)
print(prediction)
print("Predicted Flower : ", iris.target_names[prediction[0]])