# DATA QUALITY INSPECTOR
## Project Description
Data Quality Inspector is a planned web-based system designed to assess and improve the quality of structured datasets. Datasets may contain missing values, duplicate records, inconsistent categories, invalid entries, and unusual numerical values. Detecting these issues manually can be difficult and time-consuming, potentially leading to unreliable analyses and decisions.
The system aims to help users identify data quality problems, review possible improvements, and make informed decisions about cleaning their datasets.
## Objective
The main objective is to develop a web-based system that evaluates dataset quality, detects common data issues, and recommends appropriate cleaning actions. Users will be able to review and approve suggested changes before they are applied. The system is also planned to generate data quality reports and support comparisons between datasets before and after cleaning.
## Target Users
The target users are students, researchers, and data analysts who work with structured datasets. The system is intended for users who want to inspect and clean their data without writing complex code or using advanced data analysis tools.
## Planned Technologies
- Programming language: Python (planned)
- Web framework: To be determined
- Data processing tools: To be determined
- User interface: Web-based interface
- Storage approach: To be determined during implementation
The final technology stack will be selected as development progresses.
## Planned Features
- Upload CSV datasets.
- Detect common data quality issues, including missing values, duplicate records, inconsistent values, and invalid entries.
- Identify potentially unusual numerical values for user review.
- Generate data quality reports.
- Suggest possible data cleaning actions.
- Allow users to review and approve proposed changes before applying them.
- Preserve the original dataset during cleaning.
- Compare data quality before and after cleaning.

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

## Design Decisions
- The first version will focus on CSV files.
- Cleaning actions will require user approval.
- Approved cleaning actions are planned to operate on a working copy so that the original dataset remains unchanged.
- The initial storage approach will be determined during implementation.
- Technology choices remain preliminary until they are evaluated through development and testing.

## Current Status
**Week 3 – System Design and Documentation**
- Reviewed and refined the project requirements and scope.
- Prepared the proposed system methodology and description.
- Documented the preliminary system architecture and component responsibilities.
- Prepared the sequence diagram source file.
- Documented preliminary design decisions and technology considerations.
- Planned the initial prototype for Week 4.

### GitHub Issues
- [Issue #1: Define functional and non-functional requirements](https://github.com/sudeyldrm54/dataquality-inspector/issues/1) 
- [Issue #2: Prepare project scope and use cases](https://github.com/sudeyldrm54/dataquality-inspector/issues/2) 
- [Issue #3: Plan the first prototype](https://github.com/sudeyldrm54/dataquality-inspector/issues/3 ) 
