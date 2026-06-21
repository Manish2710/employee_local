import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from settings import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_USERNAME,
    SQL_PASSWORD
)

from config import logger


def get_connection():

    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
    )

    params = quote_plus(connection_string)

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )

    # Verify the connection early so failures surface with a clear message
    try:
        conn = engine.connect()
        conn.close()
        logger.info("Connected to Azure SQL Successfully")
    except Exception as e:
        logger.error("Failed to connect to Azure SQL: %s", e)
        # Re-raise to let callers decide how to handle, or they can catch this
        raise

    return engine


def write_to_sql(df):

    logger.info("Writing data to Azure SQL")

    try:
        engine = get_connection()

        df.to_sql(
            "employee_master",
            engine,
            if_exists="replace",
            index=False
        )

        logger.info("Data successfully loaded")

    except Exception as e:
        logger.error("Error writing to Azure SQL: %s", e)

        # Fallback: write to CSV in logs/ with timestamp
        from datetime import datetime
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        fallback_path = f"logs/employee_master_fallback_{ts}.csv"
        try:
            df.to_csv(fallback_path, index=False)
            logger.info("Wrote fallback CSV to %s", fallback_path)
        except Exception as csv_e:
            logger.error("Failed to write fallback CSV: %s", csv_e)
            raise