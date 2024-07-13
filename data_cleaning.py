import pandas as pd
import numpy as np
from Exception import DataCleaningError

def clean_data(filepath):
    try:
      df = pd.read_csv(filepath)
      print(df)
      df.shape
      df.isnull().sum()
      df.drop('cause', inplace=True, axis=1)
      df.columns
      df.duplicated().sum()
      df.info()
      list=['SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC DISEASE']
      for i in list:
        df[i] = df[i].astype('int')
      df.info()
      df.describe()

      return df
    except KeyError as e:
       raise DataCleaningError(f"Critical column missing: {e}")
    except Exception as e:
       raise DataCleaningError(f"Error in data cleaning: {e}")
       