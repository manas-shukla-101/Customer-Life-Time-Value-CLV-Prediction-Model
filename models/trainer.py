import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Tuple, Optional
from utils.logger import get_logger
from utils.helpers import safe_str
from config import RANDOM_STATE, TEST_SIZE, N_ESTIMATORS, MAX_DEPTH, MIN_SAMPLES_SPLIT

logger = get_logger(__name__)

def prepare_data(rfm: pd.DataFrame) -> Tuple:
    """Prepare data for modeling."""
    try:
        logger.info("Preparing data for modeling")
        
        X = rfm[['Recency', 'Frequency', 'Monetary', 'AvgOrderValue', 'PurchaseInterval']]
        y = rfm['CLV']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
        )
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler
        
    except Exception as e:
        logger.error(f"Error preparing data: {safe_str(e)}")
        return None

def train_model(X_train, y_train) -> Optional[RandomForestRegressor]:
    """Train Random Forest model."""
    try:
        logger.info("Training Random Forest model")
        
        model = RandomForestRegressor(
            n_estimators=N_ESTIMATORS,
            max_depth=MAX_DEPTH,
            min_samples_split=MIN_SAMPLES_SPLIT,
            random_state=RANDOM_STATE,
            n_jobs=-1,
            verbose=1
        )
        
        model.fit(X_train, y_train)
        logger.info("Model training complete")
        return model
        
    except Exception as e:
        logger.error(f"Error training model: {safe_str(e)}")
        return None