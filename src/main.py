from src.database import engine
from src.logger import logger
from src.datasets import DATASETS
from src.etl.extract import extract_csv
from src.etl.transform import convert_dates
from src.etl.load import load_dataframe
from src.quality.checks import (
    get_shape,
    count_nulls,
    count_duplicates,
)
from src.quality.report import (
    generate_report,
)
from src.utils.timer import Timer

def main():
    timer = Timer()
    timer.start_timer()
    logger.info("Starting ETL pipeline")
    results = []

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
            nulls = count_nulls(df)
            duplicates = count_duplicates(
                df,
                dataset["primary_key"]
            )

            results.append({
                "table": dataset["table"],
                "rows": rows,
                "columns": cols,
                "duplicates": duplicates,
                "nulls": {
                    column: int(value)
                    for column, value in nulls.items()
                    if value > 0
                },
            })

            # Load
            load_dataframe(
                df=df,
                table_name=dataset["table"],
                engine=engine
            )

        except Exception as e:
            logger.exception(f"Error processing table '{dataset['table']}'")

    execution_time = timer.stop_timer()
    generate_report(
        results,
        execution_time,
    )

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()