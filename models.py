import pandas as pd



def load_data(data):
    df = pd.read_csv(data)
    return df 