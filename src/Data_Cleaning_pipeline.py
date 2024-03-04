import pandas as pd
import numpy as np
import re
from typing import Tuple
from typing import Annotated
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from src.constants import Data_Path_Pre, Data_Path_Post
from src.Preprocessing import *

def pipeline() -> Tuple[
        Annotated[pd.DataFrame, 'X_train_scaled'],
        Annotated[pd.DataFrame, 'X_test_scaled'],
        Annotated[pd.Series, 'y_train'],
        Annotated[pd.Series, 'y_test']
]:

    df1, df2 = Data_Ingestion(Data_Path_Pre, Data_Path_Post)
    combined_df = pd.concat([df1, df2], axis = 1)
    combined_df = combined_df.drop(['index', 'index'], axis = 1)
    combined_df = combined_df.drop(['Ext_Intcode', 'Ext_Intcode', 'Ext_Intcode', 'Ext_Intcode'], axis = 1)
    combined_df['Cruise Distance'] = combined_df['Cruise Distance'].apply(clean_cruise_distance)
    combined_df['Cruise Distance'] = combined_df['Cruise Distance'].abs()
    Num_cols = list(combined_df.select_dtypes(['int64', 'float64']).columns)
    impute_null_with_mode(combined_df)
    impute_null_with_mean(combined_df, Num_cols)
    combined_df = combined_df.drop(['Logging', 'Date of Birth'], axis = 1)
    Obj_cols = list(combined_df.select_dtypes('object').columns)
    le = LabelEncoder()
    for col in Obj_cols:
        combined_df[f'{col}'] = le.fit_transform(combined_df[f'{col}'])
    X = combined_df.drop(columns=['Ticket Type'])  
    y = combined_df['Ticket Type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
