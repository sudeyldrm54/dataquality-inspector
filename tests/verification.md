# Preliminary Verification

These checks do not replace the full testing and validation planned for Week 6.

| ID | Input/action | Expected | Actual | Status |
|---|---|---|---|---|
| P01 | test.csv (5 rows, 2 missing values, 1 duplicate row) | 5 rows, 3 columns, 2 missing values, 1 duplicate row | 5 rows, 3 columns, 2 missing values (13.33%), 1 duplicate row | Pass |
| P02 | empty.csv (0 bytes) | Understandable empty-file error message | "The uploaded CSV file is empty" message displayed | Pass |
| P03 | header_only.csv (header, no data rows) | File read, warning that there are no data rows | 0 rows, 3 columns, warning displayed, no quality check performed | Pass |
| P04 | latin1.csv (Latin-1 encoded) | File read via encoding fallback without error | 2 rows, 2 columns, no error | Pass |
| P05 | fake.csv (plain text saved as .csv) | Readable error or warning that the file is not a valid dataset | Accepted as a dataset with 1 row and 1 column; no warning | Limitation observed |
| P06 | clean.csv (no issues) | 0 missing values, 0 duplicates, "no duplicates" message | 0 missing values (0.00%), 0 duplicates, message displayed | Pass |

## Notes
- P05: the file can technically be parsed by pandas, so no error is raised. The application does not yet check whether the content looks like a meaningful dataset. This is recorded as a limitation for a later week.
