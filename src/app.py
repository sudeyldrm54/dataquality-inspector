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

        # ---------- Dataset information (FR-01) ----------
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

        # ---------- Data quality check (FR-02) ----------
        st.subheader("Data Quality Check")

        if df.empty:
            st.warning("The file contains no data rows, so no quality check was performed.")
        else:
            # Missing values
            missing_per_column = df.isna().sum()
            total_missing = int(missing_per_column.sum())
            total_cells = df.shape[0] * df.shape[1]
            missing_percent = (total_missing / total_cells) * 100

            # Duplicate rows (the first occurrence is not counted)
            duplicate_mask = df.duplicated()
            duplicate_count = int(duplicate_mask.sum())

            m1, m2, m3 = st.columns(3)
            with m1:

                st.metric("Total Missing Values", total_missing)
            with m2:
                st.metric("Missing Value Ratio", f"{missing_percent:.2f}%")
            with m3:
                st.metric("Duplicate Rows", duplicate_count)

            st.markdown("**Missing values per column**")
            missing_table = pd.DataFrame({
                "Column": missing_per_column.index,
                "Missing Count": missing_per_column.values,
                "Missing %": (missing_per_column.values / df.shape[0] * 100).round(2)
            })
            st.dataframe(missing_table, use_container_width=True)

            if duplicate_count > 0:
                st.markdown("**Duplicate rows**")
                st.dataframe(df[duplicate_mask], use_container_width=True)
            else:
                st.info("No duplicate rows were found.")

    except pd.errors.EmptyDataError:
        st.error("The uploaded CSV file is empty. Please upload a file containing data.")

    except Exception as error:
        st.error(f"Could not read the file: {error}")
