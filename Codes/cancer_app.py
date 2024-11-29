import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Title
st.title("Breast Cancer Dataset Explorer")

# Load the dataset
@st.cache_data
def load_data():
    cancer_data = load_breast_cancer()
    df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
    df['target'] = cancer_data.target
    df['target'] = df['target'].map({0: 'Malignant', 1: 'Benign'})
    return df, cancer_data

# Load data
df, cancer_data = load_data()

# Display dataset
st.write("### Breast Cancer Dataset")
st.dataframe(df)

# Dataset insights
st.write("### Dataset Information")
st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])

# Summary statistics
st.write("### Summary Statistics")
st.write(df.describe())

# Sidebar options
st.sidebar.header("Filter Options")
selected_target = st.sidebar.multiselect("Select Diagnosis (Target)", df['target'].unique(), default=df['target'].unique())

# Filter dataset
filtered_df = df[df['target'].isin(selected_target)]

# Display filtered dataset
st.write("### Filtered Dataset")
st.dataframe(filtered_df)

# Visualization options
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter Plot", "Histogram"])

if chart_type == "Scatter Plot":
    st.write("### Scatter Plot")
    x_axis = st.sidebar.selectbox("X-Axis", cancer_data.feature_names)
    y_axis = st.sidebar.selectbox("Y-Axis", cancer_data.feature_names)
    st.write(f"Scatter plot: {x_axis} vs {y_axis}")
    st.scatter_chart(filtered_df[[x_axis, y_axis]])
elif chart_type == "Histogram":
    st.write("### Histogram")
    hist_column = st.sidebar.selectbox("Select Column for Histogram", cancer_data.feature_names)
    st.write(f"Histogram of {hist_column}")
    st.bar_chart(filtered_df[hist_column])

# Display dataset target classes
st.write("### Target Classes")
st.write({0: "Malignant", 1: "Benign"})
