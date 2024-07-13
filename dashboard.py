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
