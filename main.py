from sqlalchemy import create_engine  
from sqlalchemy import text
import logging
#from transform_data import df_table, df_total_category, table_total_source, df_cine_total, tranform
#from load_data import *
from extraction_data import download_data
from transform_data import transform
#from load_data import DB_load
from config import DATABASE_URI

def DB_create ():
    engine = create_engine(DATABASE_URI)

    with engine.connect() as con:
        with open('tables.sql') as file:
            query = text(file.read())
            con.execute(query)


if __name__ ==  "__main__":
    """_main_
    """
    #configure logging format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Init process...')
    DB_create ()
    data_downloaded = download_data()
    data_transformation = transform(data_downloaded)
    print(data_transformation)
    #DB_load(data_transformation)
    logging.info('Finish process...')




    

