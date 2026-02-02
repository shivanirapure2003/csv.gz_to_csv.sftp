import gzip
import shutil
import os
from glob import glob

input_dir = "data"
output_dir = "silverdata"

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get all .csv.gz.sftp files
files = glob(os.path.join(input_dir, "*.csv.gz.sftp"))

for file_path in files:
    file_name = os.path.basename(file_path)
    
    output_file = file_name.replace(".csv.gz.sftp", ".csv.sftp")
    output_path = os.path.join(output_dir, output_file)

    with gzip.open(file_path, "rb") as f_in:
        with open(output_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
# add something
    print(f"Converted: {file_path} -> {output_path}")
