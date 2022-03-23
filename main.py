from sqlalchemy import create_engine  
from sqlalchemy import text
import logging
from extraction_data import *
from transform_data import *
import psycopg2
DATABASE_URI = 'postgresql://postgres:postgres@localhost/'

def DB_create ():
    engine = create_engine(DATABASE_URI)

    with engine.connect() as con:
        with open('table.sql') as file:
            query = text(file.read())
            con.execute(query)


if __name__ ==  "__main__":
    """_main_
    """
    logging.getLogger("Create DB")
    DB_create()
    

