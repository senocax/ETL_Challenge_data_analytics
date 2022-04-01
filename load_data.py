from transform_data import df_table, df_cine_total,df_total_category, table_total_source
from sqlalchemy import create_engine
import pandas as pd
from main import sql_insert_csv
import psycopg2

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
