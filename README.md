# 🚀 Intelligent Flaky Test Detector

This project detects flaky test cases by analyzing execution history and other key features. Using **XGBoost** and effective feature engineering, we achieved **high accuracy** in identifying flaky tests.

---

## 🛠️ Technologies Used
- **Python**
- **Feature Engineering**
- **XGBoost**
- **Docker**

---

## 🌟 Features
- **Fluctuation Count** – Tracks the pass/fail history of test cases over time.  
- **Code Changes Before Fail** – Identifies code files linked to failed tests.  
- **Commit History** – Analyzes the project's commit logs.  
- **File Change Frequency** – Counts how often each file is modified.  
- **File Authors** – Tracks the number of contributors to each file.  
- **Config File Changes** – Detects commits that modify only configuration files.  

---


## 🚀 How to Run
1. Clone the repo
2. Download Docker 
3. Navigate to the project repo and run the following to build the image.
```
docker build -t flaky-test-detector .
```
4. Run the following command to train the model:
```
docker run --rm -v $(pwd):/app flaky-test-detector train
```
5. Run the following command to test the model:
```
docker run --rm -v $(pwd):/app flaky-test-detector train
```

##  ⚠️ Limitations
The dataset is small. Despite a lot of searching, we couldn’t find real-world test execution history.

## 🎯 Accuracy Results
We achieved **84% accuracy**, but with a larger real-world dataset, this could be improved significantly.

## 🔮Future Work
Integrating this model into CI/CD pipelines could help avoid running flaky tests, saving **time and resources**.