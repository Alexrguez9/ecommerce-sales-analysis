import pandas as pd
from src.transform import convert_dates

def test_convert_dates():
    df = pd.DataFrame({
        "date": [
            "2024-01-01",
            "2024-02-01"
        ]
    })
    result = convert_dates(df,["date"])
    assert pd.api.types.is_datetime64_any_dtype(
        result["date"]
    )

def test_convert_dates_keeps_other_columns():
    df = pd.DataFrame({
        "date": [
            "2024-01-01"
        ],
        "name": [
            "Alex"
        ]
    })
    result = convert_dates(df,["date"])
    assert "name" in result.columns

def test_convert_dates_invalid_date():
    df = pd.DataFrame({
        "date": [
            "invalid"
        ]
    })
    result = convert_dates(df,["date"])
    assert result["date"].isna().sum() == 1