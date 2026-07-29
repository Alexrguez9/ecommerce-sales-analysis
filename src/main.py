from database import engine
from logger import logger
from extract import extract_csv
from transform import convert_dates
from load import load_dataframe
from datasets import DATASETS

def main():
    logger.info("Starting ETL pipeline")
    for dataset in DATASETS:
        df = extract_csv(dataset["file"])

        df = convert_dates(
            df,
            dataset["dates"]
        )

        load_dataframe(
            df,
            dataset["table"],
            engine
        )
    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()