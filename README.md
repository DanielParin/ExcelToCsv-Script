# Excel to CSV Conversion Script

## Description

This script reads an Excel file and converts it into a CSV format with a semicolon delimiter. It uses the `pandas` library to load the Excel file and export the data to a CSV file.

## Requirements

Before running the script, make sure you have the necessary libraries installed. You can install them via `pip`:

```bash
pip install pandas
```

## Usage

1. Ensure you have Python installed on your system.
2. Modify the `excel` variable in the script to point to the file you want to process.
3. Modify the `csv` variable in the script with the name you want.
4. Place your Excel file in the same directory as the script or specify the full path to the file.
5. Run (where is located) the script using:

   ```sh
   python CsvScript.py

## Notes

- The script creates the CSV in the same location as the Excel file.
- Backup your file before running the script if necessary.
