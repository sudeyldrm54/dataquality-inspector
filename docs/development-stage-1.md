# Development Stage 1

| Field | Entry |
|---|---|
| Date | 02.11.2026 |
| Objective | Build the first working prototype of the Data Quality Inspector |
| Implemented functionality | CSV upload (FR-01), encoding fallback (UTF-8, then Latin-1), dataset summary and preview, missing value and duplicate row detection (FR-02), error handling for empty or unreadable files (NFR-02) |
| Related GitHub Issue | #4 |
| Important technical decision | Streamlit and pandas were used for rapid development of a web interface and for tabular data handling. Processing is done in memory and the original data is only read, not modified (NFR-03). |
| Problem encountered | 1) IndentationError caused by incorrectly indented except blocks. 2) The new quality check section did not appear because the application was still running the old code. 3) fake.csv (plain text) is accepted as a valid dataset. |
| Solution attempted | 1) Corrected the indentation of the try/except blocks. 2) Saved the file and restarted the Streamlit application. 3) Not solved yet, recorded as a limitation for a later week. |
| Related GitHub commit | 33625ed (CSV upload and preview, FR-01); 6fafbad (missing value and duplicate detection, FR-02); 6facae2 (preliminary verification results) |
| Screenshot/other evidence | evidence/week-04/p01-normal-file.png to p06-clean-file.png; test results in tests/verification.md |
| Next development step | Week 5: generate a structured data quality report (FR-03) and start cleaning suggestions (FR-04) |
