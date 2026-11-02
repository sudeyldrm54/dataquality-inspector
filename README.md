# DATA QUALITY INSPECTOR

## Project Description
Data Quality Inspector is a web-based system designed to assess and improve the quality of structured datasets. Datasets may contain missing values, duplicate records, inconsistent categories, invalid entries, and unusual numerical values. Detecting these issues manually can be difficult and time-consuming, potentially leading to unreliable analyses and decisions. The system aims to help users identify data quality problems, review possible improvements, and make informed decisions about cleaning their datasets.

## Objective
The main objective is to develop a web-based system that evaluates dataset quality, detects common data issues, and recommends appropriate cleaning actions. Users will be able to review and approve suggested changes before they are applied. The system is also planned to generate data quality reports and support comparisons between datasets before and after cleaning.

## Target Users
The target users are students, researchers, and data analysts who work with structured datasets. The system is intended for users who want to inspect and clean their data without writing complex code or using advanced data analysis tools.

## Technologies
- Programming language: Python
- Web framework: Streamlit
- Data processing: pandas
- User interface: Web-based interface (Streamlit)
- Storage approach: In-memory processing during the user session (no database in the initial version)

## Features

### Implemented (Week 4 prototype)
- Upload a CSV dataset (FR-01).
- Automatic encoding fallback (UTF-8, then Latin-1).
- Dataset summary: file name, number of rows and number of columns.
- Preview of the first 10 rows.
- Detection of missing values (total, ratio, and per column) (FR-02).
- Detection of duplicate rows (FR-02).
- Error messages for empty or unreadable files (NFR-02).
- The original data is only read, not modified.

### Planned
- Detect inconsistent values and invalid entries.
- Identify potentially unusual numerical values for user review.
- Generate structured data quality reports (FR-03).
- Suggest possible data cleaning actions (FR-04).
- Allow users to review and approve proposed changes before applying them (FR-05).
- Preserve the original dataset during cleaning.
- Compare data quality before and after cleaning (FR-06).

## Scope

### In Scope
- CSV file upload and validation.
- Detection and reporting of common data quality issues.
- Cleaning suggestions for user review.
- Basic data quality summaries.
- Comparison of results before and after approved cleaning actions.

### Out of Scope (Initial Version)
- Real-time data processing.
- Distributed or big-data processing.
- Advanced machine-learning-based automatic correction.
- Automatic data collection from external sources.
- Excel support in the initial version.

## System Architecture
The proposed system follows a modular architecture with separate components for:
- User Interface
- File Handling
- Error Message Handling
- Data Quality Analysis
- Report Generation
- Cleaning and Comparison

In the Week 4 prototype, the User Interface, File Handling, Error Message Handling, and an initial version of the Data Quality Analysis component are implemented.

## Design Decisions
- The first version focuses on CSV files.
- Cleaning actions will require user approval.
- Approved cleaning actions are planned to operate on a working copy so that the original dataset remains unchanged.
- Data is processed in memory; no database is used in the initial version.
- Streamlit and pandas were selected for rapid prototyping of a web interface and tabular data handling.

## How to Run the Prototype
Requirements: Python 3 and the packages listed in `requirements.txt`.
pip install -r requirements.txt
streamlit run src/app.py
Then open the local address shown in the terminal (usually http://localhost:8501).
To generate the sample test files:
python tests/make_test_files.py

## Project Structure
src/                          Application source code
tests/                        Test data generator and verification results
docs/architecture/            Architecture diagrams (Week 3)
docs/development-stage-1.md   Development Stage 1 record
evidence/week-04/             Screenshots and output evidence

## Current Status

### Week 4 – First Working Prototype
- Implemented CSV upload with validation and error handling (FR-01, NFR-02).
- Implemented dataset summary and preview.
- Implemented missing value and duplicate row detection (FR-02).
- Ran six preliminary verification checks (see `tests/verification.md`).
- Known limitation: a plain text file saved with a .csv extension is accepted as a dataset, because it can be parsed by pandas.
- Next step: structured quality report (FR-03) and cleaning suggestions (FR-04).

## GitHub Issues
- [Issue #1: Define functional and non-functional requirements](https://github.com/sudeyldrm54/dataquality-inspector/issues/1)
- [Issue #2: Prepare project scope and use cases](https://github.com/sudeyldrm54/dataquality-inspector/issues/2)
- [Issue #3: Plan the first prototype](https://github.com/sudeyldrm54/dataquality-inspector/issues/3)
- [Issue #4: Implement FR-01 and FR-02 prototype](https://github.com/sudeyldrm54/dataquality-inspector/issues/4)
