import pandas as pd
from logger import logger

def extract_csv(file_path: str) -> pd.DataFrame:
    logger.info(f"Reading {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"{len(df)} rows loaded.")
    return df
