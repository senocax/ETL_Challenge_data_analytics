from sqlalchemy import create_engine
from sqlalchemy import text
from config import DATABASE_URI
from sqlalchemy import exc
import csv
from io import StringIO
import pandas as pd
import logging

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
        print(type(e))
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

def DB_load(total_dataframe, engine):
    """ convert dataframe to sql

    Args:
        total_dataframe (object): list of dataframe
        engine (objet): instance engine database
    """
    table_principal = total_dataframe[0]
    table_category = total_dataframe[2][0]
    table_source = total_dataframe[3]
    table_province_category = total_dataframe[2][1]
    cine_result = total_dataframe[1]

    #create table principal 
    table_principal.to_sql('table_principal', engine, if_exists='replace', method=sql_insert_csv, index=False)
    #create table count category
    table_category.to_sql('table_category', engine, if_exists='replace', method=sql_insert_csv, index=False)
    #create table max order for source
    table_source.to_sql('table_source', engine, if_exists='replace', method=sql_insert_csv, index=False)
    #create table order count for province and category
    table_province_category.to_sql('table_province_category', engine, if_exists='replace', method=sql_insert_csv, index=False, )
    #create table cine
    cine_result.to_sql('cine_result', engine, if_exists='replace', method=sql_insert_csv, index=False)
    logging.info('Load data to DB successfull')

