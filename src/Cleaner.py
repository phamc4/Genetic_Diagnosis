import pandas as pd
import numpy as np

def data_cleaner(df):
    
    #Encode Categorical Features
    df['type'] = (df['type'] == 'normal').astype(int)
    
    #Drop Columns
    df.drop(columns='samples', inplace=True)
    
    #Rename target header
    df.rename({'type': 'target'}, inplace=True)
    
    return df

def labels(df):
    #Get the target labels in the dataframe
    labels = [i for i in df['type'].unique()]
    
    return labels