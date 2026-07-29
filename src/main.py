from database import engine
from logger import logger
from datasets import DATASETS
from extract import extract_csv
from transform import convert_dates
from quality import (
    check_shape,
    check_nulls,
    check_duplicates
)
from load import load_dataframe

def main():
    logger.info("Starting ETL pipeline")
    for dataset in DATASETS:
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
        check_shape(df)
        check_nulls(df)
        check_duplicates(
            df,
            dataset["primary_key"]
        )

        # Load
        load_dataframe(
            df=df,
            table_name=dataset["table"],
            engine=engine
        )

    logger.info("ETL pipeline finished successfully")


if __name__ == "__main__":
    main()