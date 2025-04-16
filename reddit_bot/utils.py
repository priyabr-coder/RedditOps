import pandas as pd
import os

def save_usernames_to_csv(user_data, filename="data/usernames.csv"):
    df = pd.DataFrame(user_data)
    df.to_csv(filename, index=False)
