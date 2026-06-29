from flask import Flask, jsonify, request # imports Flask class, jsonify() converts a python dictionary into JSON
# request contains everything the client sent
from flask_cors import CORS
import pickle # for loading model.pkl into memory
from sklearn.datasets import load_iris

app = Flask(__name__) # this creates your flask application

CORS(app)

# Load the trained model once when Flask starts
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# convert prediction (0, 1, 2) to flower name
    iris = load_iris()
    flower_names = iris.target_names# single flower prediction

# Registering all server routes
@app.route("/") # this is called decorator -> it simply mean when someone visits /, run the function below
def home(): # this function executes when browser visits port 5000
    return "Backend is running!" # flask sends this text back to the browser as the response

# BUILDING OUR FIRST API
@app.route("/api/test")
def test():
    return jsonify({ # flask automatically converts it to JSON, sets the correct headers, and sends it to React
        "status": "success",
        "message": "Flask backend is working!"
    })

# CREATE PREDICT ROUTE
@app.route("/predict", methods=["POST"]) # type of request received is post that means react sent data to flask server
def predict():
    data = request.get_json() # requests entire package set by client and in that JSON is in the body so we get JSON using get_json()
    # flask stores it in request obj, and we json from that and store it in data variable
    # request.get_json() means read the JSON data from the body of the request and convert it into a python dictionary
    # now flask can access values like data["sepal_length"] etc
    
    # print(data)

    # create input for the model
    features = [[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]]
    # KNN model expects input [[], [], []] like this for many flowers not only one

    # predict using loaded model
    prediction = model.predict(features)
    # this predict() returns numpy array
    # if one flower input then array([2]) - virginica
    # if multiple flowers then array([0, 2]) - first one is setosa and second is virginica

    flower = flower_names[prediction[0]]

    return jsonify({
        # "message": "Predict API is working!"
        "prediction" : flower
    })

if __name__ == "__main__": # run this server only if this file is executed directly
    app.run(host="0.0.0.0", port=10000)