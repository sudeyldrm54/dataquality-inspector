import streamlit as st
import pandas as pd
from io import BytesIO

from data_quality import (
    analyze_missing_values,
    build_missing_table,
    analyze_duplicates,
    generate_quality_report,
    generate_cleaning_suggestions
)

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
            df = pd.read_csv(
                BytesIO(file_data),
                encoding="utf-8-sig"
            )
        except UnicodeDecodeError:
            df = pd.read_csv(
                BytesIO(file_data),
                encoding="latin-1"
            )

        st.success("File uploaded successfully!")

        # Plausibility check for single-column files (e.g., plain text saved as .csv)
        if df.shape[1] < 2:
            st.warning(
                "The uploaded file contains only one column. "
                "Please verify that it is a properly structured tabular CSV dataset."
            )

        # Dataset Information (FR-01)
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

        # Data Quality Check (FR-02)
        st.subheader("Data Quality Check")

        if df.empty:
            st.warning(
                "The file contains no data rows, "
                "so no quality check was performed."
            )
        else:
            missing_per_column, total_missing, missing_percent = (
                analyze_missing_values(df)
            )
            duplicate_mask, duplicate_count = analyze_duplicates(df)

            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Total Missing Values", total_missing)
            with m2:
                st.metric("Missing Value Ratio", f"{missing_percent:.2f}%")
            with m3:
                st.metric("Duplicate Rows", duplicate_count)

            # Missing Values Per Column
            st.markdown("**Missing values per column**")
            missing_table = build_missing_table(df, missing_per_column)
            st.dataframe(missing_table, use_container_width=True)

            # Duplicate Rows
            if duplicate_count > 0:
                st.markdown("**Duplicate rows**")
                st.dataframe(df[duplicate_mask], use_container_width=True)
            else:
                st.info("No duplicate rows were found.")

            # Structured Quality Report (FR-03)
            st.subheader("Structured Data Quality Report")
            st.write(
                "This report summarizes the quality issues "
                "detected in the uploaded dataset."
            )

            report_data = generate_quality_report(
                df,
                total_missing,
                missing_percent,
                duplicate_count
            )

            st.dataframe(
                report_data,
                use_container_width=True,
                hide_index=True
            )

            if total_missing == 0 and duplicate_count == 0:
                st.success(
                    "The dataset passed the performed quality checks."
                )
            else:
                st.warning(
                    "The dataset contains quality issues "
                    "that may require attention."
                )

            # Download Report
            report_csv = report_data.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                label="Download Quality Report",
                data=report_csv,
                file_name="data_quality_report.csv",
                mime="text/csv"
            )

            # Cleaning Suggestions (FR-04)
            st.subheader("Cleaning Suggestions")
            st.write(
                "The following suggestions are based on the "
                "detected data quality issues. "
                "No changes are automatically applied to your dataset."
            )

            suggestions_df = generate_cleaning_suggestions(
                df,
                missing_per_column,
                duplicate_count
            )

            if not suggestions_df.empty:
                st.dataframe(
                    suggestions_df,
                    use_container_width=True,
                    hide_index=True
                )
                st.info(
                    "These are recommendations only. "
                    "Your original dataset has not been modified."
                )
            else:
                st.success(
                    "No cleaning suggestions are necessary. "
                    "No missing values or duplicate rows were detected."
                )

    except pd.errors.EmptyDataError:
        st.error(
            "The uploaded CSV file is empty. "
            "Please upload a file containing data."
        )

    except Exception as error:
        st.error(f"Could not read the file: {error}")
