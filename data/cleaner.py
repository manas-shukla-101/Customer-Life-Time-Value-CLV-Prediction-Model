import pandas as pd
from typing import Optional
from utils.logger import get_logger
from utils.helpers import safe_str

logger = get_logger(__name__)

def clean_data(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Clean and preprocess raw retail data."""
    try:
        logger.info("Starting data cleaning")
        
        # Convert dates
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
        df = df[df['InvoiceDate'].notna()]
        
        # Filter valid transactions
        df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]
        df = df[df['Customer ID'].notna()]
        df['Customer ID'] = df['Customer ID'].astype(str)
        
        # Calculate monetary value
        df['TotalPrice'] = df['Quantity'] * df['Price']
        
        logger.info(f"Cleaned {len(df)} records")
        logger.info(f"{df['Customer ID'].nunique()} unique customers")
        
        return df
        
    except Exception as e:
        logger.error(f"Error cleaning data: {safe_str(e)}")
        return None