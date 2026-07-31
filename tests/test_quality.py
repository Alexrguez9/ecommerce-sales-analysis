import pandas as pd
from src.quality import (
    get_shape,
    count_nulls,
    count_duplicates
)

def test_get_shape():
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["A", "B"]
    })
    assert get_shape(df) == (2, 2)

def test_count_nulls():
    df = pd.DataFrame({
        "id": [1, None],
        "name": ["A", None]
    })
    result = count_nulls(df)
    assert result["id"] == 1
    assert result["name"] == 1

def test_count_duplicates():
    df = pd.DataFrame({
        "id": [1, 1, 2]
    })
    duplicates = count_duplicates(df,["id"])
    assert duplicates == 1

def test_count_duplicates_without_duplicates():
    df = pd.DataFrame({
        "id": [1, 2, 3]
    })
    duplicates = count_duplicates(df,["id"])
    assert duplicates == 0