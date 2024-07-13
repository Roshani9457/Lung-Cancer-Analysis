## Lung Cancer Analysis

## Description of Dataset
This project is an interactive online application that uses Streamlit to generate a dashboard for data visualisation related to lung cancer, based on Python. The dataset contains variables for age, gender, anxiety, chronic illness, smoking habits, and lung cancer symptoms. Data analysis, file management, exception handling, data cleaning, and visualisation are all covered by modules on the dashboard. Lung cancer trends can be predicted and understood by users by loading data from a CSV file, displaying the dataset, and exploring important insights through a variety of plots and charts.

## Columns used for Data Visualization:
-GENDER : Gender of patient
-AGE : Age of patient
-LUNG_CANCER : Display patient is positive or negative

## How to run the Code
To run the program based on this project, follow these steps:

## 1. Setup the Environment:
    -> Ensure proper/required version of Python is installed on your system.
    -> Install required libraries using by pip:
        pip install pandas
        pip install matplotlib
        pip install streamlit

## 2. Use the Dataset
    - Use the 'survey_lung_cancer_cleaned_data.csv' dataset for the project.  

## 3. Run the Application
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Execute the following command:
        streamlit run dashboard.py
    - This command will start a local server and open the application in your default web browser.   

# Data Cleaning (data_cleaning.py)
The data cleaning process involves loading the dataset, handling missing values, removing duplicates.

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
       

# Exception (Exception.py)
Custom exceptions are defined in 'Exception.py 'and are handled throughout the project to manage errors effectively.

import os
import pandas as pd 
class DataCleaningError(Exception):
    def __init__(self, message="Error during data cleaning"):
        self.message = message
        super().__init__(self.message)
        

# File Handling (file_handling.py)
File handling functions are used open the file and write the data into survey_lung_cancer_cleaned_data.csv
File handling functions are used for saving cleaned data and loading data from files.

import pandas as pd
from Exception import DataCleaningError

def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Loaded DataFrame from CSV:")
        print(df.head())
        return df
    except FileNotFoundError as e:
        raise DataCleaningError(f"File not found: {filepath}") from e

def save_csv(df, filepath):
    try:
        df.to_csv(filepath, index=False)
        print(f"DataFrame successfully saved to {filepath}")
    except Exception as e:
        raise DataCleaningError(f"Failed to save file: {filepath}") from e


# Dashboard (dashboard.py)
Creates a Streamlit dashboard for user interactive data visualization.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from file_handling import load_csv
from analysis import analysis
import base64


df=load_csv("survey_lung_cancer_cleaned_data.csv")
analysis_result=analysis(df)

def print_data(df):
    st.title("Lung Cancer Analysis")
    st.write("---------------------------------------------------------------")
    st.markdown(
    """
    <style>
        .big-font {
            text-align: justify;
            font-size:20px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.markdown('<p class="big-font">This project is an interactive online application that uses Streamlit to generate a dashboard for data visualisation related to lung cancer, based on Python. The dataset contains variables for age, gender, anxiety, chronic illness, smoking habits, and lung cancer symptoms. Data analysis, file management, exception handling, data cleaning, and visualisation are all covered by modules on the dashboard. Lung cancer trends can be predicted and understood by users by loading data from a CSV file, displaying the dataset, and exploring important insights through a variety of plots and charts.</p>', unsafe_allow_html=True)
    st.header(("Original DataSet:"))
    st.write(df)
    st.header("Analysis:")
    st.markdown(f'<p class="big-font">Male with Lung Cancer:{analysis_result["Male_Lung_Cancer"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Female with Lung Cancer:{analysis_result["female_Lung_Cancer"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Average age of individuals with Lung Cancer:{round(analysis_result["Average_age_Lung_Cancer"],2)}</p>', unsafe_allow_html=True)


def plot_data(df):
    st.header("Plotting")
    st.write("---------------------------------------------------------------")
    st.subheader("Lung Cancer Distribution for Gender:")
    g=st.selectbox("Select gender:",options=['M','F'])
    g_df = df[df['GENDER'] == g]
    lung_cancer_count = g_df['LUNG_CANCER'].value_counts()
    plt.bar(lung_cancer_count.index, lung_cancer_count.values, color='lightgreen')
    plt.xlabel('Lung Cancer')
    plt.ylabel('Count')
    st.pyplot(plt)

    st.subheader("Lung Cancer Disturbution on all columns:")
    a = st.selectbox("Select:", df.columns, index=15)
    st.subheader("Bar Chart")
    st.bar_chart(df[a].head(25), color='#90EE90')


st.sidebar.title("Menu")
st.sidebar.text("---------------------------------")
d = st.sidebar.radio('Select', ["Main", "Plotting"])

if d=="Main":
    print_data(df)
elif d=="Plotting":
    plot_data(df)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background: rgba(255, 255, 255, 0.5) url("data:image/png;base64,%s") no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('6dbe81c7-52c8-41ae-ac52-85c663fe6821.jfif')

# Analysis (analysis.py) 
Organize/Arrange data cleaning, visualization, and dashboard creation.

import pandas as pd
import numpy as np
from file_handling import load_csv,save_csv
from Exception import DataCleaningError
from data_cleaning import clean_data

file_path="E:\\nimu\\project\\survey_lung_cancer.csv"
cleaned_data=clean_data(file_path)
save_csv(cleaned_data,"E:\\nimu\\project\\survey_lung_cancer_cleaned_data.csv")

load_cleaned_data=load_csv("E:\\nimu\\project\\survey_lung_cancer_cleaned_data.csv")

def analysis(lcd):
    lung_cancer_counts = lcd['GENDER'].groupby(lcd['LUNG_CANCER']).value_counts()
    lung_cancer_yes_counts = lung_cancer_counts.loc['YES']
    # lung_cancer_no_counts = lung_cancer_counts.loc['NO']

    male_with_lung_cancer = lung_cancer_yes_counts.loc['M'] if 'M' in lung_cancer_yes_counts.index else 0
    female_with_lung_cancer = lung_cancer_yes_counts.loc['F'] if 'F' in lung_cancer_yes_counts.index else 0
    print(f"Male with Lung Cancer: {male_with_lung_cancer}")
    print(f"Female with Lung Cancer: {female_with_lung_cancer}")
    lung_cancer_yes_data = lcd[lcd['LUNG_CANCER'] == 'YES']
    average_age_with_lung_cancer = lung_cancer_yes_data['AGE'].mean()
    print(f"Average age of individuals with Lung Cancer: {average_age_with_lung_cancer:.2f}")
    
    return{
        "Male_Lung_Cancer":male_with_lung_cancer,
        "female_Lung_Cancer":female_with_lung_cancer,
        "Average_age_Lung_Cancer":average_age_with_lung_cancer
    }
    
    
if __name__ == "__main__":
    analysis(load_cleaned_data)
    