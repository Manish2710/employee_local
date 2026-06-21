from sqlalchemy import create_engine
from urllib.parse import quote_plus
from config import logger
from settings import SQL_SERVER, SQL_DATABASE, SQL_USERNAME, SQL_PASSWORD
import pyodbc
import traceback

print('pyodbc drivers:', pyodbc.drivers())

# Add a short connection timeout parameter to fail fast if network/firewall blocks
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SQL_SERVER};"
    f"DATABASE={SQL_DATABASE};"
    f"UID={SQL_USERNAME};"
    f"PWD={SQL_PASSWORD};"
    f"Encrypt=yes;TrustServerCertificate=no;"
    f"Connection Timeout=5;"
)

print('Using connection string with driver 17 (timeout=5s)')
engine = create_engine("mssql+pyodbc:///?odbc_connect=" + quote_plus(conn_str))
try:
    with engine.connect() as conn:
        print('Connected successfully using driver 17')
except Exception:
    print('Driver 17 connection failed:')
    traceback.print_exc()
    # try driver 18
    conn_str18 = conn_str.replace('ODBC Driver 17 for SQL Server', 'ODBC Driver 18 for SQL Server')
    print('Trying driver 18 (timeout=5s)')
    engine2 = create_engine("mssql+pyodbc:///?odbc_connect=" + quote_plus(conn_str18))
    try:
        with engine2.connect() as conn:
            print('Connected successfully using driver 18')
    except Exception:
        print('Driver 18 connection failed:')
        traceback.print_exc()
