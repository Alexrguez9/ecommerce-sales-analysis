from sqlalchemy.engine import Engine
import pandas as pd
from logger import logger

def load_dataframe(
    df: pd.DataFrame,
    table_name: str,
    engine: Engine,
):

    logger.info(f"Loading {table_name}...")
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
    )
    logger.info(f"{table_name} loaded successfully.")