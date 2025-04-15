import pandas as pd
import os

def save_usernames_to_csv(usernames, path="data/usernames.csv"):
    df = pd.DataFrame({"username": list(set(usernames))})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
