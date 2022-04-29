from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import exc
import csv
from io import StringIO
import pandas as pd
import logging

# Config postgreSQL Database
# "postgres://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
database_user = config['DEFAULT']['DB_USER']
database_password = config['DEFAULT']['DB_PASSWORD']
database_name = config['DEFAULT']['DB_NAME']
database_host = config['DEFAULT']['DB_HOST']

DATABASE_URI = f'postgresql://{database_user}:{database_password}@{database_host}/'

def DB_create ():
    """create DB with read

    Returns:
      engine : instance engine db
    """
    engine = create_engine(DATABASE_URI)
    logging.info('Connecting to the PostgreSQL database')
    try:
        with engine.connect() as con:
            with open('tables.sql') as file:
                query = text(file.read())
                con.execute(query)
    except exc.SQLAlchemyError as e:
        logging.info(type(e))
    return engine

def sql_insert_csv(table, conn, keys, data_iter):
    """insert data into database

    Args:
        table (object): table name
        conn (objcet): connection
        keys (str): columns name
        data_iter (str): rows string of  data
    """
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)