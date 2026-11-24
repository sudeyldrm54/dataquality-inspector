# Week 6 – Testing and Validation

## Tasks Completed
- Designed 23 test cases: 5 unit (UT), 6 integration (IT), 6 system/UI (ST), 6 boundary (BT).
- Wrote `tests/test_data_quality.py` (unittest) with CSV fixtures in `test_data/`.
- Ran the 23 automated tests (UT, IT, BT): **23 passed, 0 failed** (`python -m unittest tests.test_data_quality -v`).
- Measured analysis time on `BT06_large_dataset.csv` (10,000 rows × 5 columns): 0.0062 s (file read and UI rendering not included).
- Wrote the Week 6 testing report and Development Stage 4 record.

## Problems Found
- A whitespace-only cell (`unittest5.csv`) is not counted as a missing value, because pandas reads it as text. The tool reports 1 missing value instead of 2.
- No test failed in the final run, so no failure → fix → retest cycle is claimed.

## Next Steps
- Run ST-01 to ST-06 manually and record the results.
- Decide whether to fix the whitespace limitation and retest.
- Week 7: installation/run instructions, README update, integration; later FR-05 and FR-06.
