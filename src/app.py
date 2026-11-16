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
            st.warning(
                "The file contains no data rows, "
                "so no quality check was performed."
            )

        else:
            # Missing values
            missing_per_column = df.isna().sum()
            total_missing = int(missing_per_column.sum())
            total_cells = df.shape[0] * df.shape[1]

            missing_percent = (
                (total_missing / total_cells) * 100
                if total_cells > 0 else 0
            )

            # Duplicate rows
            duplicate_mask = df.duplicated()
            duplicate_count = int(duplicate_mask.sum())

            m1, m2, m3 = st.columns(3)

            with m1:
                st.metric("Total Missing Values", total_missing)

            with m2:
                st.metric(
                    "Missing Value Ratio",
                    f"{missing_percent:.2f}%"
                )

            with m3:
                st.metric("Duplicate Rows", duplicate_count)

            # Missing values per column
            st.markdown("**Missing values per column**")

            missing_table = pd.DataFrame({
                "Column": missing_per_column.index,
                "Missing Count": missing_per_column.values,
                "Missing %": (
                    missing_per_column.values / df.shape[0] * 100
                ).round(2)
            })

            st.dataframe(
                missing_table,
                use_container_width=True
            )

            # Duplicate rows
            if duplicate_count > 0:
                st.markdown("**Duplicate rows**")
                st.dataframe(
                    df[duplicate_mask],
                    use_container_width=True
                )
            else:
                st.info("No duplicate rows were found.")

            # ---------- Structured Quality Report (FR-03) ----------
            st.subheader("Structured Data Quality Report")

            st.write(
                "This report summarizes the quality issues "
                "detected in the uploaded dataset."
            )

            report_data = pd.DataFrame({
                "Quality Check": [
                    "Dataset Information",
                    "Missing Values",
                    "Duplicate Rows"
                ],
                "Result": [
                    f"{df.shape[0]} rows and {df.shape[1]} columns",
                    f"{total_missing} missing values ({missing_percent:.2f}%)",
                    f"{duplicate_count} duplicate rows"
                ],
                "Status": [
                    "Completed",
                    "Issues Found" if total_missing > 0 else "Passed",
                    "Issues Found" if duplicate_count > 0 else "Passed"
                ]
            })

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

            # Download report
            report_csv = report_data.to_csv(index=False).encode("utf-8-sig")

            st.download_button(
                label="Download Quality Report",
                data=report_csv,
                file_name="data_quality_report.csv",
                mime="text/csv"
            )

            # ---------- Cleaning Suggestions (FR-04) ----------
            st.subheader("Cleaning Suggestions")

            st.write(
                "The following suggestions are based on the "
                "detected data quality issues. "
                "No changes are automatically applied to your dataset."
            )

            suggestions = []

            # Suggestions for missing values
            for column in df.columns:
                missing_count = int(df[column].isna().sum())

                if missing_count > 0:
                    if pd.api.types.is_numeric_dtype(df[column]):
                        if df[column].notna().any():
                            mean_value = df[column].mean()
                            suggestions.append({
                                "Column": column,
                                "Detected Issue": f"{missing_count} missing values",
                                "Suggested Action": (
                                    f"Fill missing values with the mean "
                                    f"({mean_value:.2f})"
                                )
                            })
                        else:
                            suggestions.append({
                                "Column": column,
                                "Detected Issue": f"{missing_count} missing values",
                                "Suggested Action": (
                                    "No valid numeric values available "
                                    "to calculate a mean"
                                )
                            })
                    else:
                        mode_values = df[column].mode(dropna=True)

                        if not mode_values.empty:
                            mode_value = mode_values.iloc[0]
                            suggestions.append({
                                "Column": column,
                                "Detected Issue": f"{missing_count} missing values",
                                "Suggested Action": (
                                    f"Fill missing values with the most "
                                    f"frequent value ({mode_value})"
                                )
                            })
                        else:
                            suggestions.append({
                                "Column": column,
                                "Detected Issue": f"{missing_count} missing values",
                                "Suggested Action": (
                                    "No existing value available "
                                    "for filling"
                                )
                            })

            # Suggestion for duplicate rows
            if duplicate_count > 0:
                suggestions.append({
                    "Column": "All columns",
                    "Detected Issue": f"{duplicate_count} duplicate rows",
                    "Suggested Action": (
                        "Review and consider removing duplicate rows"
                    )
                })

            if suggestions:
                suggestions_df = pd.DataFrame(suggestions)

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

