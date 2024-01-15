# import libraries
from pathlib import Path

# assign data related paths to variables for cleanly accessing them in notebooks
data_dir = Path("../data/") # working directory will be either "notebooks" or "scripts", so I include "../" for going to parent directory to be able to navigate to "data/"
raw_data_dir = data_dir / "raw/"
raw_data = raw_data_dir / "heart_failure_clinical_records_dataset.csv" 