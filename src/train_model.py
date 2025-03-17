import numpy as np
from sklearn.model_selection import train_test_split
from data_loader import load_data
from feature_extraction import extract_features
import xgboost as xgb
import joblib  

test_exec, testcase_to_code, code_changes, commit_history, labels = load_data()
features = extract_features(test_exec, testcase_to_code, code_changes, commit_history)
labels = labels["LABEL"]

X_train, X_test, y_train, y_test = train_test_split(
    features, 
    labels, 
    test_size=0.3, 
    stratify=labels, 
    random_state=42)

np.save("X_test.npy", X_test)  
np.save("y_test.npy", y_test)  

model = xgb.XGBClassifier(
    objective="binary:logistic",  # Binary classification -> Flaky 1 or Not Flaky 0 testcases
    eval_metric="logloss",  
    use_label_encoder=False,
    n_estimators=100,  # num of trees
    learning_rate=0.1,  # step size shrinkage
    max_depth=6,  # maximum depth of trees
)

model.fit(X_train, y_train)

joblib.dump(model, "models/intelligent_flaky_testcases_detector.pkl")
print("model saved successfully")
