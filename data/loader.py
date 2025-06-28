import os
import pandas as pd
import numpy as np
from typing import Optional
from utils.logger import get_logger
from config import DATA_PATH, ENCODING, SAMPLE_SIZE

logger = get_logger(__name__)

def load_raw_data(file_path: Optional[str] = None) -> Optional[pd.DataFrame]:
    """Load and validate dataset from CSV."""
    try:
        final_path = file_path or DATA_PATH
        if not final_path or not os.path.exists(final_path):
            raise FileNotFoundError(f"File not found: {final_path}")
            
        logger.info(f"Loading data from: {final_path}")
        df = pd.read_csv(final_path, encoding=ENCODING)
        
        if len(df) < 1000:
            raise ValueError("Dataset too small")
            
        logger.info(f"Loaded {len(df)} records")
        return df
        
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None

def create_sample_data() -> pd.DataFrame:
    """Generate synthetic sample data."""
    np.random.seed(42)
    data = {
        'Invoice': [f'INV-{i:05d}' for i in range(1000, 1000+SAMPLE_SIZE)],
        'StockCode': [f'SKU-{np.random.randint(1000,9999)}' for _ in range(SAMPLE_SIZE)],
        'Description': [f'Product {chr(65+i%26)}' for i in range(SAMPLE_SIZE)],
        'Quantity': np.random.randint(1, 20, SAMPLE_SIZE),
        'InvoiceDate': pd.date_range('2020-01-01', periods=SAMPLE_SIZE, freq='h'),
        'Price': np.round(np.random.uniform(1, 100, SAMPLE_SIZE), 2),
        'Customer ID': [f'CUST-{np.random.randint(1000,1100)}' for _ in range(SAMPLE_SIZE)],
        'Country': np.random.choice(['UK','US','Germany','France','Australia'], SAMPLE_SIZE)
    }
    df = pd.DataFrame(data)
    df['TotalPrice'] = df['Quantity'] * df['Price']
    return df