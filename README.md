# 🌸 Iris Flower Classification using K-Nearest Neighbors (KNN)

## 📖 Overview

This project is a beginner-friendly Machine Learning application built using Python and Scikit-learn.

The model learns from the famous Iris dataset and predicts the species of an Iris flower based on four flower measurements provided by the user.

This project was built to understand the complete Machine Learning workflow, including data loading, preprocessing, model training, prediction, and evaluation.

---

# 📂 Dataset

The project uses the built-in Iris dataset available in Scikit-learn.

The dataset contains **150 flower samples** belonging to three different species:

* Setosa
* Versicolor
* Virginica

Each flower has four features:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

Target labels:

| Label | Species    |
| ----: | ---------- |
|     0 | Setosa     |
|     1 | Versicolor |
|     2 | Virginica  |

---

# 🛠 Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn

---

# 📌 Machine Learning Workflow

```text
                Iris Dataset
                     │
                     ▼
            Load Dataset
                     │
                     ▼
         Separate Features (X)
         and Target Labels (y)
                     │
                     ▼
     Split into Training and Testing Data
          (80% Train, 20% Test)
                     │
                     ▼
       Create KNN Classification Model
                     │
                     ▼
          Train Model using fit()
                     │
                     ▼
      Predict Test Data using predict()
                     │
                     ▼
      Compare Predictions with Actual Labels
                     │
                     ▼
            Calculate Accuracy
                     │
                     ▼
      Predict User-Entered Flower Species
```

---

# 📊 Project Workflow Explained

### 1. Load Dataset

The Iris dataset is loaded from Scikit-learn.

---

### 2. Separate Features and Labels

Features (X):

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target (y):

* Flower Species

---

### 3. Train-Test Split

The dataset is divided into:

* 80% Training Data
* 20% Testing Data

The training data teaches the model.

The testing data evaluates how well the model performs on unseen data.

---

### 4. Model Selection

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm.

KNN predicts the class of a new flower by looking at the nearest flowers in the training dataset and selecting the majority class.

---

### 5. Model Training

The model learns relationships between flower measurements and their corresponding species.

```python
model.fit(X_train, y_train)
```

---

### 6. Prediction

The trained model predicts the species for unseen flowers.

```python
prediction = model.predict(X_test)
```

---

### 7. Model Evaluation

The model's performance is measured using Accuracy Score.

```python
accuracy_score(y_test, prediction)
```

---

### 8. User Prediction

The application allows users to enter flower measurements manually.

Example input:

```text
Sepal Length : 5.1
Sepal Width  : 3.5
Petal Length : 1.4
Petal Width  : 0.2
```

Example output:

```text
Predicted Flower : Setosa
```

---

# 📁 Project Structure

```text
iris-flower-classification/
│
├── iris.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/iris-flower-classification.git
```

Move into the project folder:

```bash
cd iris-flower-classification
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run the following command:

```bash
python iris.py
```

Enter the requested flower measurements when prompted.

---

# 📦 Requirements

The project uses the following Python libraries:

```text
numpy
pandas
scikit-learn
```

These are listed in the `requirements.txt` file and can be installed using:

```bash
pip install -r requirements.txt
```

---

# 📈 Sample Output

```text
Accuracy : 96.67 %

Enter Sepal Length : 5.1
Enter Sepal Width  : 3.5
Enter Petal Length : 1.4
Enter Petal Width  : 0.2

Predicted Flower : Setosa
```

---

# 🚀 Future Improvements

* Add a graphical user interface (GUI)
* Build a web application using Flask or FastAPI
* Deploy the model online
* Compare KNN with other classification algorithms such as Decision Tree and Random Forest
* Visualize the dataset using graphs

---

# 👨‍💻 Learning Outcomes

This project helped me understand:

* Machine Learning workflow
* Classification problems
* Train-Test Split
* K-Nearest Neighbors (KNN)
* Model Training
* Prediction
* Accuracy Evaluation
* User Input Prediction
* Working with Scikit-learn
