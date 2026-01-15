import pandas as pd
from pydantic import BaseModel, Field
from typing import Annotated




class Terrorist(BaseModel):
    name: str
    location: str
    danger_rate: Annotated[int, Field(
        ge=0,
        le=10
    )]

def load_data(data):
    df = pd.read_csv(data)
    return df 


def sort_data(df):
    sort_df = df.sort_values(by='danger_rate', ascending=False).head(5)
    return sort_df






