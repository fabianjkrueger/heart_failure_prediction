# import libraries
from pathlib import Path

# assign data related paths to variables for cleanly accessing them in notebooks
data_dir = Path("data/") 
raw_data_dir = data_dir / "raw/"
raw_data = raw_data_dir / "heart_failure_clinical_records_dataset.csv" 