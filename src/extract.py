import pandas as pd


def extract_csv(file_path: str) -> pd.DataFrame:
    print(f"Leyendo {file_path}")
    df = pd.read_csv(file_path)
    print(f"{len(df)} registros encontrados.")
    return df
