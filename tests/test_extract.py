import pandas as pd
from src.etl.extract import extract_csv

def test_extract_csv_returns_dataframe():
    df = extract_csv("data/raw/customers_dataset.csv")
    assert isinstance(df, pd.DataFrame)


def test_extract_csv_is_not_empty():
    df = extract_csv("data/raw/customers_dataset.csv")
    assert len(df) > 0


def test_extract_csv_contains_expected_columns():
    df = extract_csv("data/raw/customers_dataset.csv")
    assert "customer_id" in df.columns
    assert "customer_city" in df.columns