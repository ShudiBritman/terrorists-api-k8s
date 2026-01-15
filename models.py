import pandas as pd



def load_data(data):
    df = pd.read_csv(data)
    return df 


def sort_data(df):
    sort_df = df.sort_values(by='danger_rate', ascending=False).head(5)
    return sort_df





