import joblib
import os
import numpy as np
from sklearn.metrics import accuracy_score, classification_report

model = joblib.load("models/intelligent_flaky_testcases_detector.pkl")

X_test = np.load(os.path.join(os.path.dirname(__file__), "..", "X_test.npy"))
y_test = np.load(os.path.join(os.path.dirname(__file__), "..", "y_test.npy"))

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
