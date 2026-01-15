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



class DataProcessor:

    @staticmethod
    def load_data(data):
        df = pd.read_csv(data)
        return df 

    @staticmethod
    def sort_data(df):
        sort_df = df.sort_values(by='danger_rate', ascending=False).head(5)
        return sort_df

    @staticmethod
    def abbreviated_table_builder(sort_df):
        abbreviated_table: Terrorist = sort_df[['name', 'location', 'danger_rate']]
        return abbreviated_table
    @staticmethod
    def convert_to_json(df):
        df = df.to_json(orient="index")
        return df


def main(data):
    df = DataProcessor.load_data(data)
    sort_df = DataProcessor.sort_data(df)
    new_df = DataProcessor.abbreviated_table_builder(sort_df)
    json_df = DataProcessor.convert_to_json(new_df)
    return json_df





