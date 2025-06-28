import pandas as pd
from utils.logger import get_logger
from utils.helpers import safe_str

logger = get_logger(__name__)

def calculate_rfm(df):
    """Enhanced RFM calculation with validation."""
    try:
        # Validate input
        required_cols = ['InvoiceDate', 'Invoice', 'TotalPrice']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
        
        rfm = df.groupby('Customer ID').agg({
            'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
            'Invoice': 'nunique',
            'TotalPrice': 'sum'
        }).rename(columns={
            'InvoiceDate': 'Recency',
            'Invoice': 'Frequency',
            'TotalPrice': 'Monetary'
        })
        
        # Calculate additional metrics
        rfm['AvgOrderValue'] = rfm['Monetary'] / rfm['Frequency']
        rfm['PurchaseInterval'] = rfm['Recency'] / rfm['Frequency']
        rfm['CLV'] = rfm['Monetary'] * 0.2  # Simple CLV projection
        
        # Remove outliers
        rfm = rfm[rfm['Monetary'] < rfm['Monetary'].quantile(0.99)]
        
        logger.info(f"Calculated RFM metrics for {len(rfm)} customers")
        rfm['Segment'] = pd.qcut(
        rfm['CLV'],
        q=[0, 0.4, 0.8, 1],
        labels=['Bronze', 'Silver', 'Gold']
        )
        return rfm
        
    except Exception as e:
        logger.error(f"RFM calculation failed: {safe_str(e)}")
        return None