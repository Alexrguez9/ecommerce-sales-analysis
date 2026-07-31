from pathlib import Path
from datetime import datetime

def generate_report(results, execution_time):
    total_tables = len(results)
    total_rows = sum(result["rows"] for result in results)

    report = "# ETL Execution Report\n\n"

    report += "## Pipeline Status\n\n"
    report += "SUCCESS\n\n"

    report += f"Execution date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += f"Execution time: {execution_time:.2f} seconds\n\n"
    report += f"Tables processed: {total_tables}\n\n"
    report += f"Rows processed: {total_rows}\n\n"

    report += "---\n\n"

    report += "| Table | Rows | Columns | Duplicates |\n"
    report += "|------|------:|---------:|-----------:|\n"

    for result in results:
        report += (
            f"| {result['table']} "
            f"| {result['rows']} "
            f"| {result['columns']} "
            f"| {result['duplicates']} |\n"
        )

        nulls = result["nulls"]

        if not nulls:
            report += "No null values\n"
        else:
            report += "\nNull values\n\n"
            report += "| Column | Nulls |\n"
            report += "|--------|------:|\n"

            for column, value in nulls.items():
                report += f"| {column} | {value} |\n"

            report += "\n"

    Path("reports").mkdir(exist_ok=True)

    with open("reports/etl_report.md", "w") as file:
        file.write(report)