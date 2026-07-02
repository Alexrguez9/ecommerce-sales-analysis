import pandas as pd

def convert_dates(df, columns):
    for column in columns:

        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )
    return df