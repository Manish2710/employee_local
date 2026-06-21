from ingestion import (
    read_employee_file,
    read_department_file
)

from preprocessing import process_data

from db_writer import write_to_sql

from settings import (
    EMPLOYEE_FILE,
    DEPARTMENT_FILE
)

from config import logger


def run_pipeline():

    logger.info("Pipeline Started")

    emp_df = read_employee_file(
        EMPLOYEE_FILE
    )

    dept_df = read_department_file(
        DEPARTMENT_FILE
    )

    final_df = process_data(
        emp_df,
        dept_df
    )

    write_to_sql(final_df)

    logger.info("Pipeline Completed")


if __name__ == "__main__":
    run_pipeline()