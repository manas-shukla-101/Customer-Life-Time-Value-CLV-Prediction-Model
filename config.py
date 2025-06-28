import os
from pathlib import Path

# Path configuration
BASE_DIR = Path(__file__).parent
DATA_PATH = os.path.join(BASE_DIR, "data/online_retail_II.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data configuration
ENCODING = "ISO-8859-1"
SAMPLE_SIZE = 5000

# Model configuration
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 200
MAX_DEPTH = 10
MIN_SAMPLES_SPLIT = 5

# Visualization
PLOT_STYLE = "seaborn"
FIG_SIZE = (15, 5)