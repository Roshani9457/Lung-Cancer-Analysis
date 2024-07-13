import pandas as pd
from Exception import DataCleaningError

def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        #Attempts to read the CSV file specified by filepath into a pandas DataFrame (df).
        print("Loaded DataFrame from CSV:")
        print(df.head())
        return df
    #Returns the loaded DataFrame if successful.
    except FileNotFoundError as e:
        raise DataCleaningError(f"File not found: {filepath}") from e

def save_csv(df, filepath):
    try:
        df.to_csv(filepath, index=False)
        #Attempts to save the DataFrame df to the CSV file specified by filepath, 
        # without including the index column.
        print(f"DataFrame successfully saved to {filepath}")
    except Exception as e:
        raise DataCleaningError(f"Failed to save file: {filepath}") from e
