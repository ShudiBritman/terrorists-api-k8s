import pandas as pd
from pydantic import BaseModel, Field
from typing import Annotated
#from db import add_all_terrorist
from fastapi import UploadFile
import io
import csv



class Terrorist(BaseModel):
    name: str
    location: str
    danger_rate: Annotated[int, Field(
        ge=0,
        le=10
    )]



class DataProcessor:

    @staticmethod
    def load_data(file: UploadFile) -> pd.DataFrame:
        for enc in ("utf-8", "cp1252", "latin-1"):
            try:
                file.file.seek(0)
                return pd.read_csv(file.file, encoding=enc)
            except UnicodeDecodeError:
                pass
        raise ValueError("Unsupported file encoding")



    @staticmethod
    def sort_data(df):
        sort_df = df.sort_values(by='danger_rate', ascending=False).head(5)
        return sort_df


    @staticmethod
    def abbreviated_table_builder(sort_df):
        abbreviated_table: pd[Terrorist] = sort_df[['name', 'location', 'danger_rate']]
        return abbreviated_table
    

    @staticmethod
    def convert_to_json(df):
        df = df.to_json(orient="records")
        return df



def main(data):
    df = DataProcessor.load_data(data)
    sort_df = DataProcessor.sort_data(df)
    new_df = DataProcessor.abbreviated_table_builder(sort_df)
    json_df = DataProcessor.convert_to_json(new_df)
    response_json = {"count": len(new_df), "top": json_df}
    #add_all_terrorist(json_df)
    return response_json



