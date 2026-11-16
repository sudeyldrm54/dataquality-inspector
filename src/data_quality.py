import pandas as pd


def analyze_missing_values(df):
    missing_per_column = df.isna().sum()
    total_missing = int(missing_per_column.sum())

    total_cells = df.shape[0] * df.shape[1]
    missing_percent = (
        (total_missing / total_cells) * 100 if total_cells > 0 else 0
    )

    return missing_per_column, total_missing, missing_percent


def build_missing_table(df, missing_per_column):
    missing_rates = (
        (missing_per_column.values / df.shape[0] * 100).round(2)
        if df.shape[0] > 0
        else 0
    )

    return pd.DataFrame({
        "Column": missing_per_column.index,
        "Missing Count": missing_per_column.values,
        "Missing %": missing_rates
    })


def analyze_duplicates(df):
    duplicate_mask = df.duplicated()
    duplicate_count = int(duplicate_mask.sum())

    return duplicate_mask, duplicate_count


def generate_quality_report(df, total_missing, missing_percent, duplicate_count):
    return pd.DataFrame({
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


def generate_cleaning_suggestions(df, missing_per_column, duplicate_count):
    suggestions = []

    for column in df.columns:
        missing_count = int(missing_per_column[column])

        if missing_count > 0:
            if pd.api.types.is_numeric_dtype(df[column]):
                if df[column].notna().any():
                    mean_value = df[column].mean()
                    action = f"Fill missing values with the mean ({mean_value:.2f})"
                else:
                    action = "No valid numeric values available to calculate a mean"
            else:
                mode_values = df[column].mode(dropna=True)

                if not mode_values.empty:
                    mode_value = mode_values.iloc[0]
                    action = f"Fill missing values with the most frequent value ({mode_value})"
                else:
                    action = "No existing value available for filling"

            suggestions.append({
                "Column": column,
                "Detected Issue": f"{missing_count} missing values",
                "Suggested Action": action
            })

    if duplicate_count > 0:
        suggestions.append({
            "Column": "All columns",
            "Detected Issue": f"{duplicate_count} duplicate rows",
            "Suggested Action": "Review and consider removing duplicate rows"
        })

    return pd.DataFrame(suggestions)
