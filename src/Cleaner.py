import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def data_cleaner(df):
    cleaned_df = df.copy()
    
    #Encode Categorical Features
    if len(cleaned_df['type'].unique()) == 2:
        cleaned_df['type'] = (cleaned_df['type'] == 'normal').astype(int)
    else:
        lb = LabelEncoder()
        cleaned_df['type'] = lb.fit_transform(cleaned_df['type'])
        
    #Drop Columns
    cleaned_df.drop(columns='samples', inplace=True)
    
    #Rename target header
    cleaned_df.rename({'type': 'target'}, axis=1, inplace=True)
        
    return cleaned_df

def labels(df):
    #Get the target labels in the dataframe
    labels = [i for i in df['type'].unique()]
    
    return labels