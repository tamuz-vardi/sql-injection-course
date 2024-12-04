import mysql.connector
from contextlib import contextmanager, suppress

from ..consts import MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, DATABASE_NAME


@contextmanager
def create_connection(host=MYSQL_HOST, user=MYSQL_USERNAME, password=MYSQL_PASSWORD, database=DATABASE_NAME):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        yield conn
    finally:
        with suppress(Exception):
            conn.commit()
            conn.close()

@contextmanager
def create_cursor(**kwargs):
    with create_connection(**kwargs) as conn:
        try:
            cursor = conn.cursor()
            yield cursor
        finally:
            with suppress(Exception):
                cursor.commit()
                curser.close()