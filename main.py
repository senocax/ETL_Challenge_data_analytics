import logging
from extraction_data import download_data
from load_data import DB_create
from transform_data import transform
from load_data import DB_load

if __name__ ==  "__main__":
    """ init main running app
        download data
        transformation data
        load data in database
    """
    #configure logging format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Init process...')
    #init process download, transformation and load data
    data_downloaded = download_data()
    data_transformation = transform(data_downloaded)
    connect = DB_create ()
    DB_load(data_transformation, connect)

    logging.info('Finish process...')




    

