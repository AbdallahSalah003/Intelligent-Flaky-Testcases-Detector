import numpy as np

def extract_features(test_exec, testcase_to_code, code_changes, commit_history):
    feature_data = []

    for index, row in test_exec.iterrows():
        tc_id = row["TC#"]
        exec_history = row.iloc[1:].values  
        
        fluctuation_count = sum(exec_history[i] != exec_history[i-1] 
                                for i in range(1, len(exec_history)) 
                                if exec_history[i] != "NA")
        
        recent_fail = 1 if exec_history[-1] == "FAIL" else 0
        if not recent_fail:
            continue
        code_file = testcase_to_code.loc[testcase_to_code["TC#"] == tc_id, "FILE"]
        code_file = code_file.values[0] if not code_file.empty else None



        failure_dates = row.index[1:][row.iloc[1:] == "FAIL"]
        recent_fail_date = failure_dates[-1] if len(failure_dates) > 0 else "0000-00-00"

        related_commits = commit_history[(commit_history["FILES_CHANGED"].str.contains(code_file)) & 
                                         (commit_history["DATE"] <= recent_fail_date)]
        code_change_before_fail = 1 if not related_commits.empty else 0

        related_changes = code_changes[code_changes["FILE"] == code_file]
        num_changes = related_changes["NO_CHANGES"].iloc[0] if not related_changes.empty else 0
        num_authors = related_changes["NO_AUTHORS"].iloc[0] if not related_changes.empty else 0


        commits_before_fail = commit_history[commit_history["DATE"] <= recent_fail_date]
        only_config_changes = int(all(commits_before_fail["FILES_CHANGED"].apply(lambda x: all(f.startswith("CONFIG_FILE") for f in x.split(',')))))
        
        feature_data.append([
            fluctuation_count, code_change_before_fail, num_changes, num_authors, only_config_changes
        ])

    return np.array(feature_data)