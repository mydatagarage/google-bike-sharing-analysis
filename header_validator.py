import os
import pandas as pd

# Configuration
EXTRACT_DIR = "./dataset/extracted_data/"  # Directory containing CSV files

# Find all CSV files in the directory
csv_files = [f for f in os.listdir(EXTRACT_DIR) if f.endswith('.csv')]

# Exit if no CSV files found
if not csv_files:
    print("No CSV files found in directory:", EXTRACT_DIR)
    exit()

print(f"Found {len(csv_files)} CSV files to validate")

# Dictionary to store headers for each file
headers = {}

# Read headers from each CSV file (first row only for efficiency)
for file in csv_files:
    file_path = os.path.join(EXTRACT_DIR, file)
    try:
        # Only read header row (nrows=0) for performance
        headers[file] = list(pd.read_csv(file_path, nrows=0).columns)
        print(f"Read headers from: {file}")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Use first file as reference for comparison
reference_file = csv_files[0]
reference = headers[reference_file]
print(f"\nUsing {reference_file} as reference with {len(reference)} columns")

# Flag to track if any mismatches found
mismatches = False

# Compare each file's headers against reference
for file, cols in headers.items():
    if cols != reference:
        mismatches = True
        # Find which columns are missing or extra
        missing = set(reference) - set(cols)
        extra = set(cols) - set(reference)
        
        print(f"Header mismatch in: {file}")
        if missing: print(f"  Missing columns: {missing}")
        if extra: print(f"  Extra columns: {extra}")

# Final status message
if not mismatches:
    print("\nAll CSV files have matching headers")
    print(f"Columns: \n{reference}")
else:
    # Show reference headers for clarity if mismatches found
    print(f"\nReference headers from {reference_file}:")
    print(", ".join(reference))
