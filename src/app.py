import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Data Quality Inspector",
    page_icon="📊",
    layout="wide"
)

st.title("Data Quality Inspector")
st.write("Upload a CSV file to inspect your dataset.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        file_data = uploaded_file.getvalue()

        try:
            df = pd.read_csv(BytesIO(file_data), encoding="utf-8-sig")
        except UnicodeDecodeError:
            df = pd.read_csv(BytesIO(file_data), encoding="latin-1")

        st.success("File uploaded successfully!")

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)


        with col1:
            st.metric("File Name", uploaded_file.name)

        with col2:
            st.metric("Number of Rows", df.shape[0])

        with col3:
            st.metric("Number of Columns", df.shape[1])

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

    except pd.errors.EmptyDataError:
        st.error("The uploaded CSV file is empty. Please upload a file containing data.")

    except Exception as error:
        st.error(f"Could not read the file: {error}")
