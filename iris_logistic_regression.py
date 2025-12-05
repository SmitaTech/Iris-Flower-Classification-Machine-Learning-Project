# Iris Flower Classification using Logistic Regression
# Beginner Friendly Machine Learning Project

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
iris = datasets.load_iris()
X = iris.data      # Features
y = iris.target    # Labels
feature_names = iris.feature_names
target_names = iris.target_names

# -----------------------------
# 2. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# 3. Train Logistic Regression Model
# -----------------------------
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# -----------------------------
# 4. Make Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 5. Accuracy Report
# -----------------------------
print("Classification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# 6. Scatter Plot (Visualization)
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Scatter Plot")
plt.grid(True)
plt.savefig("images/scatter_plot.png")
plt.show()

# -----------------------------
# 7. Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, cmap='Blues',
            xticklabels=target_names, 
            yticklabels=target_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("images/confusion_matrix.png")
plt.show()

print("Plots saved in the 'images' folder!")

