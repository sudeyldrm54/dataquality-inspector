# Design Decisions
## 1. Web-Based Application
The Data Quality Inspector is planned as a web-based application that allows users to upload datasets and review data quality analysis results through a user interface.
## 2. Modular Architecture
The system is designed with separate components for file handling, data quality analysis, report generation, cleaning suggestions, and error handling. This separation is intended to improve maintainability, testing, and future development.
## 3. CSV as the Initial Input Format
The first version will focus on CSV files. Support for additional file formats may be considered in future versions.
## 4. User-Approved Data Cleaning
The system will suggest possible cleaning actions and allow users to review them before application. Approved changes will be applied to a working copy so that the original dataset remains unchanged.
## 5. Preliminary Storage Approach
The initial design considers processing uploaded data in memory without a separate database. The final storage approach will be determined during implementation.
## 6. Scope and Future Changes
Advanced automatic correction, real-time processing, and automatic data collection from external sources are outside the planned scope of the first version. These decisions may be revised as the project develops.
