import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(
    iris.data, columns=iris.feature_names
)
iris_data['target'] = iris.target
iris_data['target_name'] = iris_data['target'].map(
    dict(enumerate(iris.target_names))
)

# Streamlit app
st.title("Iris Dataset Viewer")

# Add a description
st.write("""
This app allows you to explore the classic Iris dataset.
Use the controls to customize your view.
""")

# Show the dataset as a table
st.subheader("Iris Dataset")
if st.checkbox("Show dataset"):
    st.dataframe(iris_data)

# Filter by target species
st.subheader("Filter by Species")
species = st.multiselect(
    "Select species to filter:",
    options=iris.target_names,
    default=iris.target_names
)

filtered_data = iris_data[iris_data['target_name'].isin(species)]

# Show filtered data
st.write(f"Showing {len(filtered_data)} rows for the selected species.")
st.dataframe(filtered_data)

# Plot the data
st.subheader("Pairplot of Features")
if st.checkbox("Show pairplot (requires seaborn)"):
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.set_theme(style="ticks")
    pairplot_fig = sns.pairplot(
        filtered_data, 
        vars=iris.feature_names, 
        hue='target_name'
    )
    st.pyplot(pairplot_fig)
