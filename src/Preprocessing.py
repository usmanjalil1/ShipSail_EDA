import pandas as pd
import numpy as np
import re
from typing import Tuple
from typing import Annotated
import sqlite3

def Data_Ingestion(path1:str, path2:str) -> Tuple[
    Annotated[pd.DataFrame, 'df1'],
    Annotated[pd.DataFrame, 'df2']
]:
    conn1 = sqlite3.connect(path1)
    df1 = pd.read_sql_query("SELECT * FROM cruise_pre", conn1)  
    conn1.close()

    conn2 = sqlite3.connect(path2)
    df2 = pd.read_sql_query("SELECT * FROM cruise_post", conn2)  
    conn2.close()
    return df1, df2

def clean_cruise_distance(distance):
    if isinstance(distance, str):
        numeric_value = re.search(r'\d+', distance)
        if numeric_value:
            return float(numeric_value.group())
    return None


def impute_null_with_mean(df, columns):
    for column in columns:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)

def impute_null_with_mode(df):
    for column in df.select_dtypes(include=['object']):
        mode_value = df[column].mode()[0]
        df[column].fillna(mode_value, inplace=True)