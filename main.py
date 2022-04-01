from sqlalchemy import create_engine  
from sqlalchemy import text
import logging
from extraction_data import list_save
from transform_data import df_table, df_total_category, table_total_source, df_cine_total
from load_data import *
import csv
from io import StringIO
from config import DATABASE_URI

def DB_create ():
    engine = create_engine(DATABASE_URI)

    with engine.connect() as con:
        with open('tables.sql') as file:
            query = text(file.read())
            con.execute(query)

def sql_insert_csv(table, conn, keys, data_iter):
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


if __name__ ==  "__main__":
    """_main_
    """
    #configure logging format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Init process...')
    DB_create ()

    

