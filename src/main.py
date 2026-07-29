from src.database import engine
from src.logger import logger
from src.datasets import DATASETS
from src.extract import extract_csv
from src.transform import convert_dates
from src.quality import (
    get_shape,
    count_nulls,
    count_duplicates
)
from src.load import load_dataframe

def main():
    logger.info("Starting ETL pipeline")
    for dataset in DATASETS:
        try:
            logger.info(f"Processing table '{dataset['table']}'")

            # Extract
            df = extract_csv(
                dataset["file"]
            )

            # Transform
            df = convert_dates(
                df,
                dataset["dates"]
            )

            # Data Quality
            rows, cols = get_shape(df)
            logger.info(
                f"Dataset shape: {rows} rows x {cols} columns"
            )

            nulls = count_nulls(df)
            nulls = nulls[nulls > 0]
            if nulls.empty:
                logger.info("No null values found.")
            else:
                logger.warning(f"Null values detected:\n{nulls}")

            duplicates = count_duplicates(
                df,
                dataset["primary_key"]
            )
            if duplicates == 0:
                logger.info("No duplicated primary keys.")
            else:
                logger.warning(f"{duplicates} duplicated rows found.")

            # Load
            load_dataframe(
                df=df,
                table_name=dataset["table"],
                engine=engine
            )

        except Exception as e:
            logger.error(f"Error processing table '{dataset['table']}': {e}")

    logger.info("ETL pipeline finished successfully")


if __name__ == "__main__":
    main()