import pandas as pd
from config import logger

def read_employee_file(path):
    logger.info("Reading employee file")

    df = pd.read_csv(path)

    logger.info(f"Employee records loaded: {len(df)}")

    print(df.head())

    return df


def read_department_file(path):
    logger.info("Reading department file")

    df = pd.read_csv(path)

    logger.info(f"Department records loaded: {len(df)}")

    print(df.head())

    return df



''' import os
from typing import Any

import pandas as pd
from config import logger


def _is_local(path: str) -> bool:
    return bool(path) and os.path.exists(path)


def _is_url(path: str) -> bool:
    return isinstance(path, str) and path.startswith(("http://", "https://"))


def _read_csv(path: str) -> pd.DataFrame:
    try:
        if _is_local(path):
            logger.info("Reading local CSV: %s", path)
            return pd.read_csv(path)
        if _is_url(path):
            logger.info("Reading CSV from URL: %s", path)
            return pd.read_csv(path)
        raise ValueError(f"Unsupported path: {path!r}")
    except Exception as exc:
        logger.error("Failed to read CSV %s: %s", path, exc, exc_info=True)
        raise


def read_employee_file(path: str) -> pd.DataFrame:
    logger.info("Reading employee file")
    df = _read_csv(path)
    logger.info("Employee records loaded: %d", len(df))
    print(df.head())
    return df


def read_department_file(path: str) -> pd.DataFrame:
    logger.info("Reading department file")
    df = _read_csv(path)
    logger.info("Department records loaded: %d", len(df))
    print(df.head())
    return df '''