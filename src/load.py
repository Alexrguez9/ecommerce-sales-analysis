from sqlalchemy.engine import Engine
import pandas as pd

def load_dataframe(
    df: pd.DataFrame,
    table_name: str,
    engine: Engine,
):

    print(f"Cargando {table_name}...")
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
    )
    print(f"{table_name} cargada correctamente.")