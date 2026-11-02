# Week 4 – First Working Prototype

## Objective
Build the first working prototype of the Data Quality Inspector.

## Completed
- CSV upload with encoding fallback (UTF-8, then Latin-1) (FR-01)
- Dataset summary and preview of the first 10 rows
- Missing value and duplicate row detection (FR-02)
- Error handling for empty or unreadable files (NFR-02)
- Six preliminary verification checks (P01-P06)

## Problems encountered
- IndentationError caused by incorrectly indented except blocks; fixed.
- New quality check section did not appear because the old code was still running; fixed by saving and restarting the app.
- A plain text file saved as .csv is accepted as a dataset; not solved yet.
