# Week 5 – Core Implementation & Software Quality

## Objective
Implement structured data quality reporting and cleaning suggestions while improving code organization and reliability.

## Completed
- Separated data quality analysis, reporting, and cleaning suggestion functions into a separate module (`src/data_quality.py`)
- Structured Data Quality Report table with status summary and CSV download export (FR-03)
- Automated cleaning suggestions for missing values and duplicate rows (FR-04)
- Non-destructive inspection keeping the original dataset unchanged (NFR-03)

## Problems encountered
- Keeping all UI rendering, data analysis, and report generation in a single file (`src/app.py`) made the code harder to read and maintain; solved by separating the core functions into `src/data_quality.py`.
- Possible error or invalid calculation when an entire column has no valid values; solved by adding safety checks before calculating mean or mode suggestions.
