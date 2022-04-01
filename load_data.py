from transform_data import df_table, df_cine_total,df_total_category, table_total_source
from sqlalchemy import create_engine
import csv
from io import StringIO
import pandas as pd
import psycopg2

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

def DB_load(total_dataframe):
    final_dataframe = total_dataframe
    engine = create_engine('postgresql://postgres:postgres@localhost/')
    #create table principal
    #df_table.to_sql('table_principal', engine, if_exists='replace', method=sql_insert_csv)
    df_table.to_sql('table_principal', con=engine, if_exists='append', chunksize=1000, index=False)
    #create table count category
    df_total_category[0].to_sql('table_category', engine, if_exists='replace', method=sql_insert_csv)
    #create table max order for source
    table_total_source.to_sql('table_source', engine, if_exists='replace', method=sql_insert_csv)
    #create table order count for province and category
    df_total_category[1].to_sql('table_province_category', engine, if_exists='replace', method=sql_insert_csv)
    #create table cine
    df_cine_total.to_sql('cine_result', engine, if_exists='replace', method=sql_insert_csv)
