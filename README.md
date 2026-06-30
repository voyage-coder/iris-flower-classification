# 🌸 Iris Flower Classification

A beginner-friendly machine learning project that classifies Iris flowers using the K-Nearest Neighbors (KNN) algorithm with Scikit-learn.

[![Python](https://img.shields.io/badge/Python-35.9%25-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-32.3%25-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS](https://img.shields.io/badge/CSS-29.7%25-red)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![HTML](https://img.shields.io/badge/HTML-2.1%25-orange)](https://developer.mozilla.org/en-US/docs/Web/HTML)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [How KNN Works](#how-knn-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [License](#license)

---

## 📊 Project Overview

This project demonstrates the fundamentals of machine learning by building a classification model for the famous Iris dataset. The model learns to distinguish between three species of Iris flowers based on their physical characteristics.

### 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Algorithm** | K-Nearest Neighbors (KNN) |
| **Dataset** | Iris Dataset (150 samples) |
| **Targets** | 3 Iris species (Setosa, Versicolor, Virginica) |
| **Features** | 4 measurements (sepal length, sepal width, petal length, petal width) |
| **Language** | Python with Web Interface (HTML/CSS/JS) |
| **Library** | Scikit-learn |

---

## 📚 Dataset

### Iris Dataset Overview

| Attribute | Details |
|-----------|---------|
| **Total Samples** | 150 |
| **Samples per Class** | 50 |
| **Features** | 4 |
| **Feature Names** | Sepal Length, Sepal Width, Petal Length, Petal Width |
| **Units** | Centimeters (cm) |
| **Classes** | Setosa, Versicolor, Virginica |

### Feature Ranges

| Feature | Min | Max | Unit |
|---------|-----|-----|------|
| Sepal Length | 4.3 | 7.9 | cm |
| Sepal Width | 2.0 | 4.4 | cm |
| Petal Length | 1.0 | 6.9 | cm |
| Petal Width | 0.1 | 2.5 | cm |

---

## 🧠 How KNN Works

### KNN Algorithm Flowchart

```
                📌 K-NEAREST NEIGHBORS (KNN) FLOWCHART

┌──────────────────────────────┐
│   Start                      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Load Training Data         │
│   (Features + Labels)        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Choose value of K          │
│   (e.g., K = 3)              │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Input New Data Point       │
│   (Flower measurements)      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Calculate Distance         │
│   (Euclidean Distance)       │
│   to all training points     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Find K Nearest Neighbors   │
│   (Smallest distances)       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Majority Voting            │
│   (Most common class)        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Predict Class Label        │
│   (Setosa / Versicolor /     │
│    Virginica)                │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   End                        │
└──────────────────────────────┘
```

### KNN Parameters Comparison

| K Value | Characteristics | Use Case |
|---------|-----------------|----------|
| **K=1** | Least smooth, prone to overfitting | Small, clean datasets |
| **K=3** | More flexible, captures details | Moderate datasets |
| **K=5** | Balanced (Recommended) | Most applications |
| **K=7** | Smoother boundaries | Noisy datasets |
| **K=15+** | Very smooth, prone to underfitting | Large datasets |

---

## 📁 Project Structure

```
Iris-flower-classification/
│
├── backend/
│   ├── app.py                  # Flask backend API
│   ├── model.pkl              # Trained ML model (KNN)
│   ├── requirements.txt       # Python dependencies
│   ├── training_model.py      # (optional) model training script
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── main.jsx
│   │   ├── index.css
│   │
│   │   ├── assets/
│   │   │   ├── setosa.jpg
│   │   │   ├── versicolor.jpg
│   │   │   ├── virginica.jpg
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── .env                  # API URL (VITE_API_URL)
│
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.7+ |
| pip | Latest |
| Modern Web Browser | Chrome, Firefox, Safari, Edge, Brave|

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/voyage-coder/iris-flower-classification.git
   cd iris-flower-classification
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import sklearn; print(f'Scikit-learn version: {sklearn.__version__}')"
   ```

---

## 💻 Usage

### Python Model Training

```python
from src.model import IrisKNN
from src.preprocessor import load_iris_data

# Load and preprocess data
X_train, X_test, y_train, y_test = load_iris_data(test_size=0.2)

# Train KNN model
model = KNeighborClassifier()
model.fit(X_train, y_train)

# Make predictions
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2%}")

# Predict single sample
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
print(f"Predicted species: {prediction}")
```

### Web Interface

1. Open `web/index.html` in your browser
2. Enter flower measurements:
   - Sepal Length (cm)
   - Sepal Width (cm)
   - Petal Length (cm)
   - Petal Width (cm)
3. Click "Predict" to get predictions

---

## 📈 Model Performance

### Expected Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 95-98% |
| **Precision** | 0.95-0.99 |
| **Recall** | 0.95-0.99 |
| **Training Time** | < 1 second |
| **Prediction Time** | < 1 millisecond |

### Confusion Matrix Interpretation

```
                Predicted
              Setosa  Versicolor  Virginica
Setosa          49        1           0
Versicolor       0        48          2
Virginica        0        1           49
```

**Interpretation:**
- ✅ Diagonal values (49, 48, 49) = Correct predictions
- ⚠️ Off-diagonal values = Misclassifications
- Overall accuracy = (49+48+49) / (50+50+50) = 98%

---

## 🔄 Model Training Pipeline

```
                🌸 IRIS MODEL TRAINING PIPELINE

┌──────────────────────────────┐
│   Load Iris Dataset          │
│   (sklearn.datasets)         │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Split Data                 │
│   Train / Test Split        │
│   (80% / 20%)               │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Train ML Model            │
│   K-Nearest Neighbors (KNN) │
│   model.fit(X_train, y_train)│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Make Predictions          │
│   model.predict(X_test)     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Evaluate Model            │
│   Accuracy Score + Report   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Save Model                │
│   model.pkl (pickle file)   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Model Ready for API       │
│   Flask Backend Uses It     │
└──────────────────────────────┘
```

---

## 🌳 Decision Boundaries

### Iris Species Characteristics

| Species | Sepal Length | Petal Length | Petal Width | Color |
|---------|--------------|--------------|-------------|-------|
| **Setosa** | 4.3-5.8 cm | 1.0-1.9 cm | 0.1-0.6 cm | Purple |
| **Versicolor** | 5.5-7.0 cm | 3.0-5.1 cm | 1.0-1.8 cm | Blue |
| **Virginica** | 6.3-7.9 cm | 4.5-6.9 cm | 1.4-2.5 cm | Red |

---

## 📚 Learning Resources

| Resource | Topic | Level |
|----------|-------|-------|
| [Scikit-learn KNN](https://scikit-learn.org/stable/modules/neighbors.html) | KNN Algorithm | Beginner |
| [Iris Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) | Dataset History | Beginner |
| [Distance Metrics](https://en.wikipedia.org/wiki/Euclidean_distance) | Math Background | Intermediate |
| [Machine Learning Basics](https://www.coursera.org/learn/machine-learning) | ML Fundamentals | Beginner |

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙋 Support

Have questions? 

- 📖 Check the [documentation](https://scikit-learn.org/)
- 💬 Open an [issue](https://github.com/voyage-coder/iris-flower-classification/issues)
- 📧 Contact the maintainer

---

## 🎓 Learning Outcomes

After completing this project, you'll understand:

| Concept | Description |
|---------|-------------|
| **Supervised Learning** | Training models with labeled data |
| **Classification** | Predicting discrete categories |
| **KNN Algorithm** | Distance-based classification |
| **Train/Test Split** | Model evaluation methodology |
| **Feature Scaling** | Normalizing input features |
| **Model Evaluation** | Accuracy, precision, recall metrics |
| **Hyperparameter Tuning** | Optimizing K value |

---

## 🚀 Next Steps

1. **Master the basics:** Run the training script multiple times
2. **Experiment:** Try different K values and observe changes
3. **Visualize:** Create plots of decision boundaries
4. **Enhance:** Add new features or algorithms
5. **Deploy:** Build a web service or mobile app

---

**Happy Learning! 🌸📊✨**

*Last Updated: 2026-06-29*
