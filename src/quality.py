import pandas as pd
from logger import logger

def check_shape(df: pd.DataFrame):
    logger.info(
        f"Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns"
    )

def check_nulls(df: pd.DataFrame):
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]

    if len(nulls) == 0:
        logger.info("No null values found.")
    else:
        logger.warning(f"Null values detected:\n{nulls}")

def check_duplicates( df: pd.DataFrame, primary_key: list[str]):
    duplicates = df.duplicated(
        subset=primary_key
    ).sum()

    if duplicates == 0:
        logger.info("No duplicated primary keys.")
    else:
        logger.warning(f"{duplicates} duplicated rows found.")
