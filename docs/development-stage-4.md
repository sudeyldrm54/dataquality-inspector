# Development Stage 4 – Testing and Correction

| Record field | Content |
|---|---|
| **Date** | 24.11.2026 |
| **Objective** | Show with systematic tests that the implemented features of Data Quality Inspector work correctly, including invalid and boundary inputs, and record expected versus actual results. |
| **Requirement ID(s)** | FR-01, FR-02, FR-03, FR-04, NFR-01, NFR-02 (FR-05, FR-06 and NFR-03 are not implemented yet and were not tested) |
| **Tested Functionality** | The five functions of `data_quality.py` (`analyze_missing_values`, `analyze_duplicates`, `build_missing_table`, `generate_quality_report`, `generate_cleaning_suggestions`); their combinations in the order used by `app.py`; the Streamlit workflow (upload, information, preview, report, download, error messages); and edge inputs (empty file, empty column, single column, issue-free data, 10,000 rows). |
| **Main Files / Modules** | `src/data_quality.py`, `src/app.py`, `tests/test_data_quality.py`, `test_data/` (CSV fixtures), `make_test_files.py` |
| **Important Technical Decision** | `unittest` from the Python standard library was chosen so the tests run without extra installation. Each test reads a CSV fixture with a known correct answer, so results are reproducible. |
| **Problem Encountered** | No test failed in the final automated run, so no failure–fix–retest cycle is claimed. The tests revealed one limitation: a cell containing only whitespace (`unittest5.csv`, second row) is not counted as missing, because pandas reads it as text. The tool reports 1 missing value instead of 2, and the Age column is read as text. |
| **Diagnosis / Solution Attempted** | Cause: `analyze_missing_values()` uses `df.isna()`, which treats only empty fields as missing. Proposed correction: convert whitespace-only strings to missing values before analysis (for example, replace values matching `^\s*$` with NA). This correction is not applied yet. If it is applied, rerun the tests and record the new commit here. The Week 5 fixes (all-empty column, single-column warning) were retested by BT-02 and BT-03. |
| **Retest Result** | Not applicable for the whitespace limitation (not yet corrected). Final automated run: 23 tests, all OK, 0.043 s; analysis of 10,000 rows took 0.0062 s. |
| **Screenshot / Evidence** | Terminal output of `python -m unittest tests.test_data_quality -v` (`unittest_run_log.txt`) |
| **Next Development Step** | Complete and record the manual UI tests; decide whether to fix the whitespace limitation and retest; Week 7: write installation and run instructions, update the README, and integrate the project so another developer can install, run and test it; later: interactive cleaning approval (FR-05) and before/after summary (FR-06). |
