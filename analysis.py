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
    


