import json
import logging
import sqlite3
from sqlite3 import Error

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


def connect(db_file, rc=0):
    # Get DB connection
    try:
        db = sqlite3.connect(db_file)
    except Exception as err:
        logging.error(err)
        rc = 1

    return db, rc


def select(db, sql_stmt, rc=0):
    # Execute the SQL statement
    try:
        cur = db.cursor()
        cur.execute(sql_stmt['select'])
        rec = cur.fetchone()
        logging.debug(f"Record: {rec}")
    except Exception as err:
        logging.error(err)
        rc = 1

    return rec, rc


def update(db, sql_stmt, rc=0):
    # Update the SQL statement
    try:
        cur = db.cursor()
        logging.debug(sql_stmt['update'])
        cur.execute(sql_stmt['update'])
        db.commit()
    except Exception as err:
        logging.error(f'update: {err}')
        rc = 1

    return rc


def close(db):
    # Close the DB connection
    db.close()


def sqlstmt(sql_file, rc=0):
    # Get SQL statements - SELECT/UPDATE
    try:
        f = open(sql_file, mode='r')
        sql_stmt = json.load(f)
        f.close()
    except FileNotFoundError as err:
        logging.error(err)
        rc = 1
    except IOError as err:
        logging.error(err)
        rc = 1

    return sql_stmt, rc
