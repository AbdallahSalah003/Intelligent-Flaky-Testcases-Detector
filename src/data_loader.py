import pandas as pd

def load_data():
    """Load all dataset files into pandas DataFrames"""
    test_exec = pd.read_csv("data/test_execution_history.csv")
    testcase_to_code = pd.read_csv("data/testcase_to_code.csv")
    code_changes = pd.read_csv("data/code_file_changes.csv")
    commit_history = pd.read_csv("data/commit_history.csv")
    labels = pd.read_csv("data/testcase_labels.csv")

    return test_exec, testcase_to_code, code_changes, commit_history, labels