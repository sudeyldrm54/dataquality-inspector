from pathlib import Path

folder = Path("test_data")
folder.mkdir(exist_ok=True)

# P01: normal file with 2 missing values and 1 duplicate row
(folder / "test.csv").write_text(
    "name,age,city\n"
    "Ali,25,Istanbul\n"
    "Ayse,,Ankara\n"
    "Ali,25,Istanbul\n"
    "Mehmet,30,\n"
    "Zeynep,22,Izmir\n",
    encoding="utf-8",
)

# P02: completely empty file
(folder / "empty.csv").write_bytes(b"")

# P03: header only, no data rows
(folder / "header_only.csv").write_text("name,age,city\n", encoding="utf-8")

# P04: Latin-1 encoded file (characters that exist in Latin-1)
(folder / "latin1.csv").write_bytes(
    "isim,sehir\nÖmer,Ürgüp\nÇiçek,Ankara\n".encode("latin-1")
)

# P05: plain text renamed to .csv
(folder / "fake.csv").write_text(
    "This is not a real dataset.\nIt is just a sentence saved as csv.\n",
    encoding="utf-8",
)

# P06: clean dataset with no missing values and no duplicates
(folder / "clean.csv").write_text(
    "name,age,city\n"
    "Ali,25,Istanbul\n"
    "Ayse,31,Ankara\n"
    "Mehmet,30,Bursa\n",
    encoding="utf-8",
)

print("Test files created in the 'test_data' folder.")
