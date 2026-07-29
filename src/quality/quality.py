import pandas as pd

def get_shape(df: pd.DataFrame) -> tuple[int, int]:
    """
    Returns the number of rows and columns.
    """
    return df.shape


def count_nulls(df: pd.DataFrame) -> pd.Series:
    """
    Returns the number of null values per column.
    """
    return df.isnull().sum()


def count_duplicates(df: pd.DataFrame, primary_key: list[str]) -> int:
    """
    Returns the number of duplicated primary keys.
    """
    return df.duplicated(
        subset=primary_key
    ).sum()