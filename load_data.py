import pandas as pd
import logging
from script import sql_insert_csv

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

